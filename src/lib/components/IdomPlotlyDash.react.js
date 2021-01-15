import React, {Component} from 'react';
import PropTypes from 'prop-types';
import Layout from 'idom-client-react';

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */

export default class IdomPlotlyDash extends Component {

    constructor(props) {
        super(props);
        this.state = { updateLayoutCallback: undefined };
      }

    shouldComponentUpdate(nextProps, nextState) {
        if (nextProps.layoutUpdates) {
            nextProps.layoutUpdates.map(
                ({ pathPrefix, changes }) => nextState.updateLayoutCallback(pathPrefix, changes)
            );
        }
        return false;
    }

    render() {
        const { id, importSourceUrl, setProps } = this.props;
        return (
            <div id={id}>
                <Layout
                    saveUpdateHook={ updateLayoutCallback => this.setState({ updateLayoutCallback }) }
                    sendEvent={ event => setProps({ layoutEvent: event }) }
                    importSourceUrl={ importSourceUrl }
                />
            </div>
        );
    }
}

IdomPlotlyDash.defaultProps = {};

IdomPlotlyDash.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * An object describing a JSON patch that will update the layout's model
     */
    layoutUpdates: PropTypes.array,

    /**
     * An event sent from the layout
     */
    layoutEvent: PropTypes.object,

    /**
     * A string defining the base URL where dynamically importable web modules can be found
     */
    importSourceUrl: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
