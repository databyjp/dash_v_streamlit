# ========== (c) JP Hwang 27/7/20  ==========
from shared_funcs import load_fig
fig = load_fig()

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

app.layout = dbc.Container([
    html.H3("Houston Rockets Shot Chart - 2020 Season"),
    html.P("This chart shows the shot distribution of the NBA team Houston Rockets, based on particular areas of the court, and their expected points per shot (i.e. efficiency) from each area."),
    html.P("Use the dropdown menu to change the color scale for the shot chart."),
    dcc.Dropdown(
        id="col-dropdown",
        options=[
            {'label': 'Blue-Yellow-Red', 'value': 'RdYlBu_r'},
            {'label': 'Rose-Teal', 'value': 'Tealrose_r'},
            {'label': 'Orange-Purple', 'value': 'PuOr_r'}
        ],
        value="RdYlBu_r",
        style={'width': '200px'}
    ),
    dcc.Graph(id="main-graph", figure=fig),
])

@app.callback(
    Output('main-graph', 'figure'),
    [Input('col-dropdown', 'value')]
)
def update_fig(colorscale):
    new_fig = fig.update_traces(marker={"colorscale":colorscale})
    return new_fig


if __name__ == '__main__':
    app.run_server(debug=False)
