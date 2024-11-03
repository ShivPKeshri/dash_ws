import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv('data/gapminderDataFiveYear.csv')

year_options = [{'label':str(year), 'value':year} for year in df['year'].unique()]

app = dash.Dash()

app.layout = html.Div([
    dcc.Dropdown(id='year_choice', options=year_options, value=df['year'].min()),
    dcc.Graph(id='graph')
])

@app.callback(
    Output(component_id='graph', component_property='figure'),
    [Input(component_id='year_choice', component_property='value')]
)
def update_graph(selected_year):
    filtered_df = df[df['year'] == selected_year]
    traces = []

    for continent in filtered_df['continent'].unique():
        continent_df = filtered_df[filtered_df['continent'] == continent]
        traces.append(go.Scatter(
            x=continent_df['gdpPercap'],
            y=continent_df['lifeExp'],
            text=continent_df['country'],
            mode='markers',
            opacity=0.7,
            marker={'size':15},
            name=continent
        ))
    layout = go.Layout(
        xaxis={'type': 'log', 'title': 'GDP Per Capita'},
        yaxis={'title': 'Life Expectancy'},
        hovermode='closest'
    )
    return dict(data=traces,layout=layout)

if __name__ == '__main__':
    app.run_server()
