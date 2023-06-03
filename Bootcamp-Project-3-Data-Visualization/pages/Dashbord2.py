import dash
from dash import html, dcc, callback, Input, Output, Dash, html
from jupyter_dash import JupyterDash
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__)

# Read dataset
import os
fpath = (str(os.path.dirname(os.path.abspath(__file__)))+'RiyadhVillasAqar.csv').replace('pages', '')
df = pd.read_csv(r''+fpath+'', dtype={'column_name_of_col_16': str}, low_memory=False)


# Define the Villa categories
villa_categories = {
    'Small Villas': (50, 400),
    'Medium Villas': (400, 1000),
    'Large Villas': (1000, 3000),
    'Extra Large Villas': (3000, 6000),
    'Palaces': (6000, float('inf'))
}

# Create the dropdown options
dropdown_options = [{'label': category, 'value': category} for category in villa_categories.keys()]

# Set up the layout with background style
layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.Div([
                    html.H1("Exploring Riyadh Villa Market:"),
                    html.H4("Location Distribution, and Neighborhood Analysis")])
                , className='display-3 mt-4 mb-4')
    ]),
    dbc.Row([
        dbc.Col([
            html.Label('Select Villa Category:', className='font-weight-bold mb-2'),
            dcc.Dropdown(
                id='villa-dropdown',
                options=dropdown_options,
                value=list(villa_categories.keys())[0],
                style={'fontSize': 16}  # Adjust font size
            )
        ], width=4)
    ], className='mb-4'),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='pie-chart')
        ], width=6),
        dbc.Col([
            dcc.Graph(id='bar-chart')
        ], width=6)
    ]),
    html.Br()
], fluid=True, style={'backgroundColor': '#f8f6fa'})  # Set the background color

# Define the callback function for updating the charts
@callback(
    Output('pie-chart', 'figure'),
    Output('bar-chart', 'figure'),
    Input('villa-dropdown', 'value'),
    Input('pie-chart', 'clickData')
)
def update_charts(villa_category, clickData):
    min_space, max_space = villa_categories[villa_category]
    filtered_df = df[(df['space'] >= min_space) & (df['space'] < max_space)]
    villa_counts = filtered_df.groupby('location').size().reset_index(name='Count')
    pie_fig = px.pie(villa_counts, names='location', values='Count', title='Villa Category Count by Location')
    pie_fig.update_layout(
        title_font=dict(size=24),
        font=dict(size=12),
        width=600,
        height=400,
        legend=dict(orientation="h", x=0, y=-0.2),
        colorway=colors
    )

    if clickData:
        location = clickData['points'][0]['label']
        filtered_df = filtered_df[filtered_df['location'] == location]
    
    neighborhood_counts = filtered_df['neighbourhood'].value_counts().reset_index()
    neighborhood_counts.columns = ['neighbourhood', 'Count']
    bar_fig = px.bar(neighborhood_counts, x='neighbourhood', y='Count', title='Villa Count by Neighborhood')
    bar_fig.update_layout(
        title_font=dict(size=24),
        font=dict(size=12),
        width=600,
        height=400,
        legend=dict(orientation="h", x=0, y=-0.2),
        colorway=colors
    )
    
    # Set the color palette for the bar chart
    bar_fig.update_traces(marker_color=colors)

    return pie_fig, bar_fig

# Set the color palette
colors = ['#66c5cc', '#f6cf71', '#f89c74', '#dcb0f2', '#87c75f', '#9eb9f3', '#fe88b1', '#c9db74', '#8be4a4', '#b497e7', '#b3b3b3']
