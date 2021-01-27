from weakref import finalize
from typing import Any, Callable, Optional

from dash import Dash
from idom.widgets.utils import multiview
from idom.core.component import AbstractComponent
from idom.server.flask import PerClientStateServer, Config

from .IdomPlotlyDash import IdomPlotlyDash


_MOUNT, _CMPT = multiview()


def create_component(__constructor: Callable[[], AbstractComponent], *args: Any, **kwargs: Any) -> IdomPlotlyDash:
    view_id = _MOUNT(lambda: __constructor(*args, **kwargs))
    return IdomPlotlyDash(viewId=view_id)


def run_server(app: Dash, *args: Any, **kwargs: Any) -> None:
    idom_server_extension = PerClientStateServer(
        _CMPT,
        Config(redirect_root_to_index=False, url_prefix="/_idom")
    )
    idom_server_extension.register(app.server)
    idom_server_extension.run(*args, **kwargs)
