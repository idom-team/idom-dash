# AUTO GENERATED FILE - DO NOT EDIT

#' @export
reactpyDashComponent <- function(viewId=NULL) {

    props <- list(viewId=viewId)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ReactPyDashComponent',
        namespace = 'reactpy_dash',
        propNames = c('viewId'),
        package = 'reactpyDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
