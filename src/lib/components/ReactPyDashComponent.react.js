import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {Layout, SimpleReactPyClient} from '@reactpy/client';

/**
 * ReactPyDashComponent allows integration between Dash and ReactPy
 */
export default class ReactPyDashComponent extends Component {
    constructor(props) {
        super(props);
        this.client = new SimpleReactPyClient({
            serverLocation: {
                url: document.location.origin,
                path: document.location.pathname,
                query: `${document.location.search || '?'}view_id=${
                    this.props.viewId
                }`,
            },
        });
    }
    render() {
        return <Layout client={this.client} />;
    }
}

ReactPyDashComponent.defaultProps = {};

ReactPyDashComponent.propTypes = {
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
