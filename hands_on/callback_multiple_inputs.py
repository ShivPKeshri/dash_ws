import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/mpg.csv')

col_option = [{'label': col.title(), 'value': col} for col in df.columns]

app = dash.Dash()

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(id='xaxis', options=col_option, value='displacement')
    ], style={'width': '48%', 'display': 'inline-block'}),

    html.Div([
        dcc.Dropdown(id='yaxis', options=col_option, value='acceleration')
    ], style={'width': '48%', 'display': 'inline-block'}),

    dcc.Graph(id='graph')
])

@app.callback(Output(component_id='graph', component_property='figure'),
            [Input(component_id='xaxis', component_property='value'),
            Input(component_id='yaxis', component_property='value')])
def update_graph(x_col, y_col):
    data = [go.Scatter(x=df[x_col],
                        y=df[y_col],
                        text=df['name'],
                        mode='markers',
                        marker=dict(size=15, opacity=0.5, line={'width': 0.5, 'color': 'white'}))]
    layout = go.Layout(
        xaxis={'title': x_col.title()},
        yaxis={'title': y_col.title()},
        margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
        hovermode='closest')

    return dict(data=data, layout=layout)

if __name__ == '__main__':
    app.run_server()
