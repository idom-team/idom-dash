# AUTO GENERATED FILE - DO NOT EDIT

export reactpydashcomponent

"""
    reactpydashcomponent(;kwargs...)

A ReactPyDashComponent component.
ReactPyDashComponent allows integration between Dash and ReactPy
Keyword arguments:
- `viewId` (String; optional): The view ID for this component instance
"""
function reactpydashcomponent(; kwargs...)
        available_props = Symbol[:viewId]
        wild_props = Symbol[]
        return Component("reactpydashcomponent", "ReactPyDashComponent", "reactpy_dash", available_props, wild_props; kwargs...)
end

