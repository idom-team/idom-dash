import React, {Component} from 'react';
import PropTypes from 'prop-types';
import Layout from 'idom-client-react';

export default class IdomPlotlyDash extends Component {
    render() {
        let loc = window.location;
        let wsProtocol;
        if (loc.protocol === 'https:') {
            wsProtocol = 'wss:';
        } else {
            wsProtocol = 'ws:';
        }

        const baseWebSocketUrl = wsProtocol + '//' + loc.host + loc.pathname;
        const baseHttpUrl = loc.protocol + '//' + loc.host + loc.pathname;

        const ws = new WebSocket(
            baseWebSocketUrl + `_idom/stream?view_id=${this.props.viewId}`
        );

        function saveUpdateHook(update) {
            ws.onmessage = (event) => {
                const [pathPrefix, patch] = JSON.parse(event.data);
                update(pathPrefix, patch);
            };
        }

        function sendEvent(event) {
            ws.send(JSON.stringify(event));
        }

        return (
            <div id={'hello'}>
                <Layout
                    saveUpdateHook={saveUpdateHook}
                    sendEvent={sendEvent}
                    importSourceUrl={baseHttpUrl + '_idom/client/web_modules'}
                />
            </div>
        );
    }
}

IdomPlotlyDash.defaultProps = {};

IdomPlotlyDash.propTypes = {
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
