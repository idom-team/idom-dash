from weakref import finalize
from typing import Any, Callable, Optional

from dash import Dash
from idom.widgets.utils import multiview
from idom.core.component import AbstractComponent
from idom.server.flask import PerClientStateServer, Config

from .IdomDashComponent import IdomDashComponent


SERVER_CONFIG = Config(redirect_root_to_index=False, url_prefix="/_idom")
_MOUNT, IdomComponentView = multiview()


def create_component(__constructor: Callable[[], AbstractComponent], *args: Any, **kwargs: Any) -> IdomDashComponent:
    view_id = _MOUNT(lambda: __constructor(*args, **kwargs))
    return IdomDashComponent(viewId=view_id)


def run_server(app: Dash, *args: Any, **kwargs: Any) -> PerClientStateServer:
    idom_server_extension = PerClientStateServer(IdomComponentView, SERVER_CONFIG)
    idom_server_extension.register(app.server)
    idom_server_extension.run(*args, **kwargs)
    return idom_server_extension


def run_daemon_server(app: Dash, *args: Any, **kwargs: Any) -> PerClientStateServer:
    idom_server_extension = PerClientStateServer(IdomComponentView, SERVER_CONFIG)
    idom_server_extension.register(app.server)
    idom_server_extension.daemon(*args, **kwargs)
    return idom_server_extension
