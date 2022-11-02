from __future__ import annotations

from dataclasses import replace
from urllib.parse import parse_qs
from collections.abc import Sequence

from dash import Dash
from dash.development.base_component import Component as DashComponent
from idom.types import ComponentType
from idom.backend.flask import configure as _configure, Options
from idom import component, use_location

from .IdomDashComponent import IdomDashComponent

_NEXT_VIEW_ID = 0
_VIEW_REGISTRY: dict[str, ComponentType] = {}


def adapt_layout(component: DashComponent) -> DashComponent:
    children = component.children
    if isinstance(children, DashComponent):
        adapt_layout(children)
    elif not isinstance(children, str) and isinstance(children, Sequence):
        component.children = [
            _create_component(c) if isinstance(c, ComponentType) else adapt_layout(c)
            for c in children
        ]
    return component


def configure_app(app: Dash, options: Options | None = None) -> None:
    if options is None:
        options = Options(url_prefix="/_idom_app")
    elif hasattr(options, "url_prefix"):
        options = replace(options, url_prefix="/_idom_app")
    _configure(app.server, _router, options)


def _create_component(idom_component: ComponentType) -> IdomDashComponent:
    global _NEXT_VIEW_ID
    dash_component = IdomDashComponent(viewId=str(_NEXT_VIEW_ID))
    _VIEW_REGISTRY[_NEXT_VIEW_ID] = idom_component
    _NEXT_VIEW_ID += 1
    return dash_component


@component
def _router():
    view_id_param = parse_qs(use_location().search[1:]).get("view_id", [])
    if len(view_id_param) != 1:
        return f"Expected exactly one view_id query parameter, got {len(view_id_param)}"

    try:
        view_id = int(view_id_param[0])
    except Exception as error:
        return "Invalid view_id, expected integer"

    return _VIEW_REGISTRY.get(view_id, "unknown view_id")
