# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class IdomPlotlyDash(Component):
    """An IdomPlotlyDash component.


Keyword arguments:
- viewId (string; optional): The view ID for this component instance"""
    @_explicitize_args
    def __init__(self, viewId=Component.UNDEFINED, **kwargs):
        self._prop_names = ['viewId']
        self._type = 'IdomPlotlyDash'
        self._namespace = 'idom_plotly_dash'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['viewId']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(IdomPlotlyDash, self).__init__(**args)
