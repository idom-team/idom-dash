import dash
import dash_html_components as html

import idom
from idom_dash import create_component, run_server

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

victory_bar = idom.web.module_from_template(
    "react",
    "victory-bar@35.4.0",
    fallback="⌛",
)
VictoryBar = idom.web.export(victory_bar, "VictoryBar")


@idom.component
def ClickCount():
    count, set_count = idom.hooks.use_state(0)
    return idom.html.button(
        {"id": "click-counter", "onClick": lambda event: set_count(count + 1)}, count
    )


@idom.component
def VictoryChart():
    return VictoryBar()


app.layout = html.Div(
    [
        html.H1("Simple Click Counter"),
        create_component(ClickCount),
        html.Br(),
        html.H1("Victory Chart"),
        create_component(VictoryChart),
    ]
)

if __name__ == "__main__":
    run_server(app, "127.0.0.1", 5000)
