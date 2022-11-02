# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class IdomDashComponent(Component):
    """An IdomDashComponent component.
IdomDashComponent allows integration between Dash and IDOM

Keyword arguments:

- viewId (string; optional):
    The view ID for this component instance."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'idom_dash'
    _type = 'IdomDashComponent'
    @_explicitize_args
    def __init__(self, viewId=Component.UNDEFINED, **kwargs):
        self._prop_names = ['viewId']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['viewId']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(IdomDashComponent, self).__init__(**args)
