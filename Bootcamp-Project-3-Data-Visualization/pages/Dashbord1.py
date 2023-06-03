import dash
from dash import html, dcc, callback, Input, Output, Dash, html
from jupyter_dash import JupyterDash
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import dash_bootstrap_components as dbc

dash.register_page(__name__)

# Read dataset
import os
fpath = (str(os.path.dirname(os.path.abspath(__file__)))+'RiyadhVillasAqar.csv').replace('pages', '')
df = pd.read_csv(r''+fpath+'', dtype={'column_name_of_col_16': str}, low_memory=False)


# Set up the layout with background style
layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.Div([
                    html.H1("Analyzing Riyadh Villa Market:"),
                    html.H4("Exploring Price Variations, Neighborhood Profiles, and Property Characteristics")])
                , className='display-3 mt-4 mb-4')
    ]),
    dbc.Row([
        dbc.Col([
            html.Label('Select Location:', className='font-weight-bold mb-2'),
            dbc.RadioItems(
                id='location-radio',
                options=[{'label': location, 'value': location} for location in df['location'].unique()],
                value=df['location'].unique()[0],
                labelStyle={'display': 'block'}
            )
        ], width=4),
        dbc.Col([
            html.Label('Select Neighbourhood:', className='font-weight-bold mb-2'),
            dcc.Dropdown(
                id='neighbourhood-dropdown',
                options=[],
                value='',
                className='form-control'
            )
        ], width=4)
    ],
    align="start",
    className='mb-3'
    ),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='scatter-chart')
        ], width=6),
        dbc.Col([
            dcc.Graph(id='front-count-chart')
        ], width=6)
    ])
], fluid=True, style={'background-color': '#f8f6fa'})  # Set the background color

# Update neighbourhood dropdown options based on selected location
@callback(
    Output('neighbourhood-dropdown', 'options'),
    Output('neighbourhood-dropdown', 'value'),
    Input('location-radio', 'value')
)
def update_neighbourhood_dropdown(location):
    neighbourhood_options = [{'label': neighbourhood, 'value': neighbourhood} for neighbourhood in
                             df[df['location'] == location]['neighbourhood'].unique()]
    neighbourhood_value = df[df['location'] == location]['neighbourhood'].unique()[0] if len(
        neighbourhood_options) > 0 else ''
    return neighbourhood_options, neighbourhood_value

# Define callback for scatter chart
@callback(
    Output('scatter-chart', 'figure'),
    Input('neighbourhood-dropdown', 'value')
)
def update_scatter_chart(neighbourhood):
    filtered_df = df[df['neighbourhood'] == neighbourhood]
    scatter_fig = px.scatter(filtered_df, x="space", y="price", title='Relationship between Space and Prices')
    scatter_fig.update_layout(
        xaxis_title='Space',
        yaxis_title='Price',
        title_font=dict(size=24),
        font=dict(size=12),
        width=600,
        height=400,
        plot_bgcolor='#f8f6fa',
        paper_bgcolor='#f8f6fa',
        legend=dict(orientation="h", x=0, y=-0.2),
        colorway=colors
    )
    scatter_fig.update_traces(marker=dict(color=colors[0]))  # Set the color palette for markers
    return scatter_fig


# Define callback for front count chart
@callback(
    Output('front-count-chart', 'figure'),
    Input('location-radio', 'value'),
    Input('neighbourhood-dropdown', 'value')
)
def update_front_count_chart(location, neighbourhood):
    filtered_df = df[(df['location'] == location) & (df['neighbourhood'] == neighbourhood)]
    front_counts = filtered_df['front'].value_counts()

    bar_fig = go.Figure(data=[go.Bar(x=front_counts.index, y=front_counts.values)])
    bar_fig.update_layout(
        title='Count of Each Front in the Selected Area',
        xaxis_title='Front',
        yaxis_title='Count',
        title_font=dict(size=24),
        font=dict(size=12),
        width=600,
        height=400,
        plot_bgcolor='#f8f6fa',
        paper_bgcolor='#f8f6fa',
        legend=dict(orientation="h", x=0, y=-0.2),
        colorway=colors
    )

    return bar_fig

# Set the color palette
colors = ['#66c5cc', '#f6cf71', '#f89c74', '#dcb0f2', '#87c75f', '#9eb9f3', '#fe88b1', '#c9db74', '#8be4a4', '#b497e7', '#b3b3b3']
