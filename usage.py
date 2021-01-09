import dash

import idom

from idom_plotly_dash import IdomComponent

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

@idom.element
def ClickCount():
    count, set_count = idom.hooks.use_state(0)
    return idom.html.button({"onClick": lambda event: set_count(count + 1)}, "hello")

app.layout = IdomComponent(app, ClickCount)


if __name__ == "__main__":
    app.run_server(debug=True)
