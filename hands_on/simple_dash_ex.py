import pandas as pd
import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go

df = pd.read_csv('data/OldFaithful.csv')

scatter_data = [go.Scatter(x=df['X'], y=df['Y'], mode='markers')]
scatter_layout = go.Layout(title='Scatter example using dash')
scatter_plot = {'data':scatter_data, 'layout': scatter_layout}

app = dash.Dash()

app.layout = html.Div([
                    dcc.Graph(id='scatter_plot' ,figure=scatter_plot)
                ])

if __name__ == '__main__':
    app.run_server()
