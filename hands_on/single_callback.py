import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='text_input', value='Initial value', type='text'),
    html.Div(id='out_div')
])

@app.callback(
    Output(component_id='out_div', component_property='children'),
    [Input(component_id='text_input', component_property='value')]
)
def update_text(input_text):
    return f'You have text : {input_text}'

if __name__ == '__main__':
    app.run_server()
