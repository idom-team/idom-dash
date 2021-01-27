# AUTO GENERATED FILE - DO NOT EDIT

idomPlotlyDash <- function(viewId=NULL) {
    
    props <- list(viewId=viewId)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'IdomPlotlyDash',
        namespace = 'idom_plotly_dash',
        propNames = c('viewId'),
        package = 'idomPlotlyDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
