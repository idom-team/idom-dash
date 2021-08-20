# AUTO GENERATED FILE - DO NOT EDIT

export idomdashcomponent

"""
    idomdashcomponent(;kwargs...)

An IdomDashComponent component.
IdomDashComponent allows integration between Dash and IDOM
Keyword arguments:
- `viewId` (String; optional): The view ID for this component instance
"""
function idomdashcomponent(; kwargs...)
        available_props = Symbol[:viewId]
        wild_props = Symbol[]
        return Component("idomdashcomponent", "IdomDashComponent", "idom_dash", available_props, wild_props; kwargs...)
end

