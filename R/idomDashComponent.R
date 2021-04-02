# AUTO GENERATED FILE - DO NOT EDIT

idomDashComponent <- function(viewId=NULL, clientModuleUrl=NULL) {
    
    props <- list(viewId=viewId, clientModuleUrl=clientModuleUrl)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'IdomDashComponent',
        namespace = 'idom_dash',
        propNames = c('viewId', 'clientModuleUrl'),
        package = 'idomDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
