# AUTO GENERATED FILE - DO NOT EDIT

idomPlotlyDash <- function(id=NULL, label=NULL, value=NULL) {
    
    props <- list(id=id, label=label, value=value)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'IdomPlotlyDash',
        namespace = 'idom_plotly_dash',
        propNames = c('id', 'label', 'value'),
        package = 'idomPlotlyDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
