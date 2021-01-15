from uuid import uuid4
from threading import Thread, Event
from asyncio import set_event_loop, new_event_loop, Queue as AsyncQueue
from queue import Queue as ThreadQueue
from typing import Any, Callable, Tuple, Optional, Dict, List

import idom
from idom.core.element import AbstractElement
from idom.core.layout import Layout, LayoutUpdate, LayoutEvent
from idom.core.dispatcher import AbstractDispatcher, SingleViewDispatcher

import dash
from dash.dependencies import Input, Output

from .IdomPlotlyDash import IdomPlotlyDash


def IdomComponent(
    app: dash.Dash,
    root_element_constructor: Callable[[], AbstractElement],
    import_source_url: Optional[str] = None,
) -> IdomPlotlyDash:
    component_id = f"idom-layout-{uuid4().hex}"

    thread, get_updates, put_event = create_idom_layout_thread(root_element_constructor)
    thread.start()

    @app.callback(
        Output(component_id=component_id, component_property="layoutUpdates"),
        Input(component_id=component_id, component_property="layoutEvent"),
    )
    def update_loop(event):
        if event is not None:
            put_event(event)
        return get_updates()

    return IdomPlotlyDash(
        id=component_id,
        layoutEvent=None,
        layoutUpdates=[],
        importSourceUrl=import_source_url,
    )


def create_idom_layout_thread(
    root_element_constructor: Callable[[], AbstractElement],
    dispatcher_type: AbstractDispatcher = SingleViewDispatcher,
    dispatcher_context: Any = None,
) -> Tuple[Thread, Callable[[], LayoutUpdate], Callable[[Any], None]]:
    layout = Layout(root_element_constructor())

    update_queue = ThreadQueue()
    loop = new_event_loop()

    # we have to do this to grab the async queue from the thread after it's created
    event_queue_ref: idom.Ref[Optional[AsyncQueue]] = idom.Ref(None)
    event_queue_ref_event = Event()

    def run():
        set_event_loop(loop)

        event_queue_ref.current = event_queue = AsyncQueue()
        event_queue_ref_event.set()

        async def send(layout_update: idom.core.layout.LayoutUpdate) -> None:
            update_queue.put(layout_update)

        async def recv():
            event = await event_queue.get()
            return LayoutEvent(**event)

        async def drive_dispatcher():
            async with dispatcher_type(layout) as dispatcher:
                await dispatcher.run(send, recv, dispatcher_context)

        loop.run_until_complete(drive_dispatcher())

    def put_event(event: Any) -> None:
        event_queue_ref_event.wait()
        event_queue = event_queue_ref.current
        assert event_queue is not None, "no event queue after event was set"
        loop.call_soon_threadsafe(event_queue.put_nowait, event)

    def get_updates() -> List[Dict[str, Any]]:
        updates: List[Dict[str, Any]]= [update_queue.get()]
        while not update_queue.empty():
            updates.append(update_queue.get())
        return [{"pathPrefix": u.path, "changes": u.changes} for u in updates]

    return Thread(target=run, daemon=True), get_updates, put_event
