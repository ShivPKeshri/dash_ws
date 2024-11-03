import dash
from dash import dcc, html
from dash.dependencies import Input, Output


app = dash.Dash()

app.layout = html.Div([
    dcc.RangeSlider(id='range-slider', min=-10, max=10, step=1, value=[-1,1]),
    html.Div(id='product_out')

],style={'width':'50%'})

@app.callback(Output('product_out', 'children'),
            [Input('range-slider', 'value')])
def product(value):
    return value[0]*value[1]



if __name__ == '__main__':
    app.run_server()
