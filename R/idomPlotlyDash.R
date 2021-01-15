# AUTO GENERATED FILE - DO NOT EDIT

idomPlotlyDash <- function(id=NULL, layoutUpdates=NULL, layoutEvent=NULL, importSourceUrl=NULL) {
    
    props <- list(id=id, layoutUpdates=layoutUpdates, layoutEvent=layoutEvent, importSourceUrl=importSourceUrl)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'IdomPlotlyDash',
        namespace = 'idom_plotly_dash',
        propNames = c('id', 'layoutUpdates', 'layoutEvent', 'importSourceUrl'),
        package = 'idomPlotlyDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
