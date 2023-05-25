import dash
from dash import html

import idom
from idom_dash import adapt_layout, configure_app
from idom_dash.idom_compat import DashState

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
configure_app(app)

victory_bar = idom.web.module_from_template(
    "react",
    "victory-bar@35.4.0",
    fallback="⌛",
)
VictoryBar = idom.web.export(victory_bar, "VictoryBar")

dash_state = DashState()


@idom.component
def ClickCount():
    count, set_count = idom.hooks.use_state(0)
    return idom.html.button(
        {"id": "click-counter", "onClick": lambda event: set_count(count + 1)}, count
    )


@idom.component
def VictoryChart():
    bar_style = {"parent": {"width": "500px"}, "data": {"fill": "royalblue"}}
    return VictoryBar({"style": bar_style})


@idom.component
def ShowInputValue():
    value = my_input_value.use_state()
    return idom.html.pre(value)


app.layout = adapt_layout(
    html.Div(
        [
            dash_state.Component(),
            html.H1("Simple Click Counter"),
            ClickCount(),
            html.Br(),
            html.H1("Victory Chart"),
            VictoryChart(),
            dash.html.Div(id="my-output"),
            my_input_value.track_state(
                dash.dcc.Input(id="my-input", value="initial value", type="text")
            ),
            ShowInputValue(),

        ]
    )
)

if __name__ == "__main__":
    app.run("127.0.0.1", 5000, debug=True)
