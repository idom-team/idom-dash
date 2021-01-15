# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class IdomPlotlyDash(Component):
    """An IdomPlotlyDash component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks.
- layoutUpdates (list; optional): An object describing a JSON patch that will update the layout's model
- layoutEvent (dict; optional): An event sent from the layout
- importSourceUrl (string; optional): A string defining the base URL where dynamically importable web modules can be found"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, layoutUpdates=Component.UNDEFINED, layoutEvent=Component.UNDEFINED, importSourceUrl=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'layoutUpdates', 'layoutEvent', 'importSourceUrl']
        self._type = 'IdomPlotlyDash'
        self._namespace = 'idom_plotly_dash'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'layoutUpdates', 'layoutEvent', 'importSourceUrl']
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
