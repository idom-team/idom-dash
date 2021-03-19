from typing import Any, Callable

from dash import Dash
from flask import Flask, send_from_directory
from idom.widgets.utils import multiview
from idom.core.component import AbstractComponent
from idom.client.manage import web_modules_dir
from idom.server.flask import PerClientStateServer, Config

from .IdomDashComponent import IdomDashComponent


SERVER_CONFIG = Config(
    url_prefix="/_idom",
    serve_static_files=False,
    redirect_root_to_index=False,
)
_MOUNT, IdomComponentView = multiview()


def create_component(__constructor: Callable[[], AbstractComponent], *args: Any, **kwargs: Any) -> IdomDashComponent:
    view_id = _MOUNT(lambda: __constructor(*args, **kwargs))
    return IdomDashComponent(viewId=view_id)


def run_server(app: Dash, host: str, port: int, debug: bool = False, *args: Any, **kwargs: Any) -> PerClientStateServer:
    if debug:
        print(f"Serving at http://{host}:{port}/")
    idom_server_extension = _make_render_server(app.server)
    idom_server_extension.run(host, port, debug=debug, *args, **kwargs)
    return idom_server_extension


def run_daemon_server(app: Dash, host: str, port: int, debug: bool = False, *args: Any, **kwargs: Any) -> PerClientStateServer:
    if debug:
        print(f"Serving at http://{host}:{port}/")
    idom_server_extension = _make_render_server(app.server)
    idom_server_extension.daemon(host, port, debug=debug, *args, **kwargs)
    return idom_server_extension

def _make_render_server(server: Flask) -> PerClientStateServer:
    idom_server_extension = PerClientStateServer(IdomComponentView, SERVER_CONFIG)
    idom_server_extension.register(server)

    @server.route(f"{SERVER_CONFIG['url_prefix']}/client/web_modules/<path:path>")
    def serve_web_modules(path: str):
        return send_from_directory(str(web_modules_dir()), path)

    return idom_server_extension
