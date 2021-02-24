import dash
import dash_html_components as html

import idom
from idom_dash import create_component, run_server

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

victory = idom.install("victory@35.4.0", fallback="loading...")
material_ui = idom.install("@material-ui/core", fallback="loading...")

@idom.component
def ClickCount():
    count, set_count = idom.hooks.use_state(0)
    return idom.html.button(
        {
            "id": "click-counter",
            "onClick": lambda event: set_count(count + 1)
        },
        count
    )

@idom.component
def MaterialClickCount():
    count, set_count = idom.hooks.use_state(0)
    return idom.html.div(
        material_ui.Button(
            {
                "color": "primary",
                "variant": "contained",
                "onClick": lambda event: set_count(count + 1),
            },
            count,
        ),
    )

app.layout = html.Div(
    [
        html.H1("Simple Click Counter"),
        create_component(ClickCount),
        html.Br(),
        html.H1("Material UI (installed)"),
        create_component(MaterialClickCount),
        html.Br(),
        html.H1("Victory Charts (installed)"),
        create_component(victory.VictoryBar)
    ]
)

if __name__ == "__main__":
    run_server(app, "127.0.0.1", 5000, debug=True)
