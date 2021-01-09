# AUTO GENERATED FILE - DO NOT EDIT

export idomplotlydash

"""
    idomplotlydash(;kwargs...)

An IdomPlotlyDash component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `layoutUpdate` (Dict; optional): An object describing a JSON patch that will update the layout's model
- `layoutEvent` (Dict; optional): An event sent from the layout
- `importSourceUrl` (String; optional): A string defining the base URL where dynamically importable web modules can be found
"""
function idomplotlydash(; kwargs...)
        available_props = Symbol[:id, :layoutUpdate, :layoutEvent, :importSourceUrl]
        wild_props = Symbol[]
        return Component("idomplotlydash", "IdomPlotlyDash", "idom_plotly_dash", available_props, wild_props; kwargs...)
end

