import os
from typing import Any, Callable

from dash import Dash
from flask import Flask
from idom.config import IDOM_DEBUG_MODE
from idom.widgets import multiview
from idom.core.proto import ComponentType
from idom.server.flask import PerClientStateServer, Config, FlaskServer
from idom import Ref

from .IdomDashComponent import IdomDashComponent


IDOM_DASH_SERVER_BASE_URL = Ref(os.environ.get("IDOM_DASH_SERVER_BASE_URL", ""))
SERVER_CONFIG = Config(
    url_prefix="/_idom",
    serve_static_files=True,
    redirect_root_to_index=False,
)
_MOUNT_VIEW, IdomComponentView = multiview()


def create_component(
    __constructor: Callable[[], ComponentType], *args: Any, **kwargs: Any
) -> IdomDashComponent:
    view_id = _MOUNT_VIEW.add(None, lambda: __constructor(*args, **kwargs))
    return IdomDashComponent(viewId=view_id)


def run_server(
    app: Dash, host: str, port: int, *args: Any, **kwargs: Any
) -> PerClientStateServer:
    idom_server_extension = _make_render_server(app.server)
    idom_server_extension.run(host, port, *args, **kwargs)
    return idom_server_extension


def run_daemon_server(
    app: Dash, host: str, port: int, *args: Any, **kwargs: Any
) -> PerClientStateServer:
    idom_server_extension = _make_render_server(app.server)
    idom_server_extension.run_in_thread(host, port, *args, **kwargs)
    return idom_server_extension


def _make_render_server(server: Flask) -> FlaskServer:
    return PerClientStateServer(IdomComponentView, SERVER_CONFIG, app=server)
