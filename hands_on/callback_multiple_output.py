import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import base64

PATH = 'data/images/'

df = pd.read_csv('data/wheels.csv')

app = dash.Dash()

def encode_image(img_path):
    encoded_img = base64.b64encode(open(img_path, 'rb').read())
    return f'data:image/png;base64,{encoded_img.decode()}'


app.layout = html.Div([
    dcc.RadioItems(id='wheel',
                   options=[{'label':i , 'value':i } for i in df['wheels'].unique()],
                   value=1),
    dcc.RadioItems(id='color',
                   options=[{'label':i.title() , 'value':i } for i in df['color'].unique()],
                   value='red'),
    html.Hr(),
    html.Div(id='wheel_out'),
    html.Div(id='color_out'),
    html.Hr(),
    html.Img(id='img', src='children', height=300)
], style={'fontFamily':'helvetica', 'fontSize':18})

@app.callback(Output('wheel_out', 'children'),
            [Input('wheel', 'value')])
def callback_wheel(wheel):
    return f'Wheel type: {wheel}'

@app.callback(Output('color_out', 'children'),
            [Input('color', 'value')])
def callback_color(color):
    return f'Wheel color: {color.title()}'

@app.callback(Output('img', 'src'),
            [Input('wheel', 'value'),
            Input('color', 'value')])
def generate_img(wheel, color):
    img_name = df[(df['wheels']==wheel) & (df['color']==color)]['image'].values[0]
    img_path = PATH + img_name
    return encode_image(img_path)

if __name__ == '__main__':
    app.run_server()
