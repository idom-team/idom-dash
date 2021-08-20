import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {mountLayoutWithWebSocket} from 'idom-client-react';

let loc = window.location;
let wsProtocol;
if (loc.protocol === 'https:') {
    wsProtocol = 'wss:';
} else {
    wsProtocol = 'ws:';
}

const baseWebSocketUrl = wsProtocol + '//' + loc.host + loc.pathname;
const baseHttpUrl = loc.protocol + '//' + loc.host + loc.pathname;

/**
 * IdomDashComponent allows integration between Dash and IDOM
 */
export default class IdomDashComponent extends Component {
    constructor(props) {
        super(props);
        this.mountPoint = React.createRef();
    }
    render() {
        return <div ref={this.mountPoint} />;
    }
    componentDidMount() {
        mountLayoutWithWebSocket(
            this.mountPoint.current,
            baseWebSocketUrl + `_idom/stream?view_id=${this.props.viewId}`,
            (source, sourceType) =>
                import(
                    /* webpackIgnore: true */
                    sourceType == 'NAME'
                        ? baseHttpUrl + `_idom/modules/${source}`
                        : source
                )
        );
    }
}

IdomDashComponent.defaultProps = {};

IdomDashComponent.propTypes = {
    /**
     * The view ID for this component instance
     */
    viewId: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};
