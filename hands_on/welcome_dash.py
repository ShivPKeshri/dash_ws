import dash
from dash import dcc
from dash import html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Hey boss!'),

    dcc.Graph(
        id="bar-chart",
        figure={
            'data':[
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'BLR'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'PAT'},
            ],
            'layout':dict(title='Bar chart dash demo')
        }
    )
])

if __name__ == '__main__':
    app.run_server()
