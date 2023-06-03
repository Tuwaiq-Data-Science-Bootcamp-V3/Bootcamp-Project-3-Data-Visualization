import dash
from dash import html, dcc, callback, Input, Output, Dash, html
from jupyter_dash import JupyterDash
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output
from jupyter_dash import JupyterDash
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__)

# Read dataset
import os
fpath = (str(os.path.dirname(os.path.abspath(__file__)))+'RiyadhVillasAqar.csv').replace('pages', '')
df = pd.read_csv(r''+fpath+'', dtype={'column_name_of_col_16': str}, low_memory=False)


# Define the app layout
layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1('Villa Features Analysis', className='display-4 mt-4 mb-4'), width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.Label('Number of Rooms:', className='font-weight-bold mb-2'),
            dcc.Dropdown(
                id='rooms-dropdown',
                options=[{'label': str(i), 'value': i} for i in sorted(df['rooms'].unique())],
                placeholder='Select number of rooms',
            )
        ], width=3),
        dbc.Col([
            html.Label('Number of Bathrooms:', className='font-weight-bold mb-2'),
            dcc.Dropdown(
                id='bathrooms-dropdown',
                options=[{'label': str(i), 'value': i} for i in sorted(df['bathrooms'].unique())],
                placeholder='Select number of bathrooms',
            )
        ], width=3),
        dbc.Col([
            html.Label('Pool:', className='font-weight-bold'),
            dbc.RadioItems(
                id='pool-radio',
                options=[{'label': 'Yes', 'value': 1.0}, {'label': 'No', 'value': 0.0}],
                value=0.0,
            )
        ], width=3),
        dbc.Col([
            html.Label('Furnished:', className='font-weight-bold'),
            dbc.RadioItems(
                id='furnished-radio',
                options=[{'label': 'Yes', 'value': 1.0}, {'label': 'No', 'value': 0.0}],
                value=0.0,
            )
        ], width=3)
    ], className='mb-4'),
    dbc.Row([
        dbc.Col([
            html.Label('Garage:', className='font-weight-bold'),
            dbc.RadioItems(
                id='garage-radio',
                options=[{'label': 'Yes', 'value': 1.0}, {'label': 'No', 'value': 0.0}],
                value=0.0,
            )
        ], width=3),
        dbc.Col([
            html.Label('Duplex:', className='font-weight-bold'),
            dbc.RadioItems(
                id='duplex-radio',
                options=[{'label': 'Yes', 'value': 1.0}, {'label': 'No', 'value': 0.0}],
                value=0.0,
            )
        ], width=3),
        dbc.Col([
            html.Label('Driver Room:', className='font-weight-bold'),
            dbc.RadioItems(
                id='driverRoom-radio',
                options=[{'label': 'Yes', 'value': 1.0}, {'label': 'No', 'value': 0.0}],
                value=0.0,
            )
        ], width=3),
        dbc.Col([
            html.Label('Maid Room:', className='font-weight-bold'),
            dbc.RadioItems(
                id='maidRoom-radio',
                options=[{'label': 'Yes', 'value': 1.0}, {'label': 'No', 'value': 0.0}],
                value=0.0,
            )
        ], width=3)
    ],className='mb-4'),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='histogram')
        ], width={"size": 6, "offset": 2})
    ])
], fluid=True, style={'background-color': '#f8f6fa'})  # Set the background color to the previous design

# Set the color palette
colors = ['#66c5cc', '#f6cf71', '#f89c74', '#dcb0f2', '#87c75f', '#9eb9f3', '#fe88b1', '#c9db74', '#8be4a4', '#b497e7', '#b3b3b3']

# Define the callback function
@callback(
    Output('histogram', 'figure'),
    Input('rooms-dropdown', 'value'),
    Input('bathrooms-dropdown', 'value'),
    Input('pool-radio', 'value'),
    Input('furnished-radio', 'value'),
    Input('garage-radio', 'value'),
    Input('duplex-radio', 'value'),
    Input('driverRoom-radio', 'value'),
    Input('maidRoom-radio', 'value')
)
def update_histogram(rooms, bathrooms, pool, furnihsed, garage, duplex, driverRoom, maidRoom):
    filtered_df = df[(df['rooms'] == rooms) &
                     (df['bathrooms'] == bathrooms) &
                     (df['pool'] == pool) &
                     (df['furnihsed'] == furnihsed) &
                     (df['garage'] == garage) &
                     (df['duplex'] == duplex) &
                     (df['driverRoom'] == driverRoom) &
                     (df['maidRoom'] == maidRoom)]
    fig = px.histogram(filtered_df, x='neighbourhood', color_discrete_sequence=colors)
    fig.update_layout(
        title='Quantifying the Number of Villas in Each Neighborhood',
        xaxis_title='Neighborhood',
        yaxis_title='Count',
        title_font=dict(size=24),
        font=dict(size=12),
        width=800,
        height=500,
        legend=dict(orientation="h", x=0, y=-0.2)
    )
    return fig



'''
# Define the app layout
layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Villa Features Analysis"), className='display-3 mt-4 mb-4')
    ]),
    dbc.Row([
        dbc.Col([
            html.Label('Number of Rooms:', className='font-weight-bold mb-2'),
            dbc.Select(
                id='rooms-dropdown',
                options=[{'label': str(i), 'value': i} for i in sorted(df['rooms'].unique())],
                placeholder='Select number of rooms',
            )
        ], width=3),
        dbc.Col([
            html.Label('Number of Bathrooms:', className='font-weight-bold mb-2'),
            dbc.Select(
                id='bathrooms-dropdown',
                options=[{'label': str(i), 'value': i} for i in sorted(df['bathrooms'].unique())],
                placeholder='Select number of bathrooms',
            )
        ], width=3),
        dbc.Col([
            html.Label('Pool:', className='font-weight-bold'),
            dbc.RadioItems(
                id='pool-radio',
                options=[{'label': 'Yes', 'value': 1.0}, {'label': 'No', 'value': 0.0}],
                value=0.0,
            )
        ], width=3),
        dbc.Col([
            html.Label('Furnished:', className='font-weight-bold'),
            dbc.RadioItems(
                id='furnished-radio',
                options=[{'label': 'Yes', 'value': 1.0}, {'label': 'No', 'value': 0.0}],
                value=0.0,
            )
        ], width=3)
    ], className='mb-4'),
    dbc.Row([
        dbc.Col([
            html.Label('Garage:', className='font-weight-bold'),
            dbc.RadioItems(
                id='garage-radio',
                options=[{'label': 'Yes', 'value': 1.0}, {'label': 'No', 'value': 0.0}],
                value=0.0,
            )
        ], width=3),
        dbc.Col([
            html.Label('Duplex:', className='font-weight-bold'),
            dbc.RadioItems(
                id='duplex-radio',
                options=[{'label': 'Yes', 'value': 1.0}, {'label': 'No', 'value': 0.0}],
                value=0.0,
            )
        ], width=3),
        dbc.Col([
            html.Label('Driver Room:', className='font-weight-bold'),
            dbc.RadioItems(
                id='driverRoom-radio',
                options=[{'label': 'Yes', 'value': 1.0}, {'label': 'No', 'value': 0.0}],
                value=0.0,
            )
        ], width=3),
        dbc.Col([
            html.Label('Maid Room:', className='font-weight-bold'),
            dbc.RadioItems(
                id='maidRoom-radio',
                options=[{'label': 'Yes', 'value': 1.0}, {'label': 'No', 'value': 0.0}],
                value=0.0,
            )
        ], width=3)
    ],className='mb-4'),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='histogram')
        ], width={"size": 6, "offset": 2})
    ])
], fluid=True, style={'background-color': '#f8f6fa'})  # Set the background color to the previous design

# Set the color palette
colors = ['#66c5cc', '#f6cf71', '#f89c74', '#dcb0f2', '#87c75f', '#9eb9f3', '#fe88b1', '#c9db74', '#8be4a4', '#b497e7', '#b3b3b3']

# Define the callback function
@callback(
    Output('histogram', 'figure'),
    Input('rooms-dropdown', 'value'),
    Input('bathrooms-dropdown', 'value'),
    Input('pool-radio', 'value'),
    Input('furnished-radio', 'value'),
    Input('garage-radio', 'value'),
    Input('duplex-radio', 'value'),
    Input('driverRoom-radio', 'value'),
    Input('maidRoom-radio', 'value')
)
def update_histogram(rooms, bathrooms, pool, furnihsed, garage, duplex, driverRoom, maidRoom):
    filtered_df = df[(df['rooms'] == rooms) &
                     (df['bathrooms'] == bathrooms) &
                     (df['pool'] == pool) &
                     (df['furnihsed'] == furnihsed) &
                     (df['garage'] == garage) &
                     (df['duplex'] == duplex) &
                     (df['driverRoom'] == driverRoom) &
                     (df['maidRoom'] == maidRoom)]
    fig = px.histogram(filtered_df, x='neighbourhood', color_discrete_sequence=colors)
    fig.update_layout(
        title='Quantifying the Number of Villas in Each Neighborhood',
        xaxis_title='Neighborhood',
        yaxis_title='Count',
        title_font=dict(size=24),
        font=dict(size=12),
        width=800,
        height=500,
        legend=dict(orientation="h", x=0, y=-0.2)
    )
    return fig
'''
