# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class IdomDashComponent(Component):
    """An IdomDashComponent component.


Keyword arguments:
- viewId (string; optional): The view ID for this component instance
- clientModuleUrl (string; optional)"""
    @_explicitize_args
    def __init__(self, viewId=Component.UNDEFINED, clientModuleUrl=Component.UNDEFINED, **kwargs):
        self._prop_names = ['viewId', 'clientModuleUrl']
        self._type = 'IdomDashComponent'
        self._namespace = 'idom_dash'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['viewId', 'clientModuleUrl']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(IdomDashComponent, self).__init__(**args)
