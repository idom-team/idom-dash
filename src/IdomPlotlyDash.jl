
module IdomPlotlyDash
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1"

include("idomplotlydash.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "idom_plotly_dash",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "idom_plotly_dash.min.js",
    external_url = "https://unpkg.com/idom_plotly_dash@0.0.1/idom_plotly_dash/idom_plotly_dash.min.js",
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "idom_plotly_dash.min.js.map",
    external_url = "https://unpkg.com/idom_plotly_dash@0.0.1/idom_plotly_dash/idom_plotly_dash.min.js.map",
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
