import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from idom_plotly_dash import IdomPlotlyDash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = IdomPlotlyDash(id="my-layout")


@app.callback(
    Output(component_id='my-layout', component_property='modelPatch'),
    Input(component_id='my-layout', component_property='layoutEvent')
)
def update_output_div(event):
    return None


if __name__ == '__main__':
    app.run_server(debug=True)
