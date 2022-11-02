# AUTO GENERATED FILE - DO NOT EDIT

#' @export
idomDashComponent <- function(viewId=NULL) {
    
    props <- list(viewId=viewId)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'IdomDashComponent',
        namespace = 'idom_dash',
        propNames = c('viewId'),
        package = 'idomDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
