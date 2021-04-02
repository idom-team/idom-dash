# AUTO GENERATED FILE - DO NOT EDIT

export idomdashcomponent

"""
    idomdashcomponent(;kwargs...)

An IdomDashComponent component.

Keyword arguments:
- `viewId` (String; optional): The view ID for this component instance
- `clientModuleUrl` (String; optional)
"""
function idomdashcomponent(; kwargs...)
        available_props = Symbol[:viewId, :clientModuleUrl]
        wild_props = Symbol[]
        return Component("idomdashcomponent", "IdomDashComponent", "idom_dash", available_props, wild_props; kwargs...)
end

