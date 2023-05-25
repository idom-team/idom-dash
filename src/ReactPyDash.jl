
module ReactPyDash
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.5"

include("jl/reactpydashcomponent.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "reactpy_dash",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "reactpy_dash.min.js",
    external_url = "https://unpkg.com/reactpy_dash@0.0.5/reactpy_dash/reactpy_dash.min.js",
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "reactpy_dash.min.js.map",
    external_url = "https://unpkg.com/reactpy_dash@0.0.5/reactpy_dash/reactpy_dash.min.js.map",
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
