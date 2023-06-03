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



# Define the age categories
age_categories = {
    'New': (0, 5),
    'Almost new': (5, 10),
    'Moderate age': (10, 20),
    'Old': (20, float('inf'))
}

# Define the property features
property_features = ['driverRoom', 'outdoorRoom', 'garage', 'elevator', 'furnihsed', 'tent', 'pool', 'basement']

dropdown_options = [{'label': category, 'value': category} for category in age_categories.keys()]

layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Exploring Villas Age Categories"), className='display-3 mt-4 mb-4')
    ]),
    dbc.Row([
        dbc.Col([
            html.Label("Select Age Category:", className='font-weight-bold mb-2'),
            dcc.Dropdown(
                id='age-dropdown',
                options=dropdown_options,
                value=list(age_categories.keys())[0]
            )
        ], width=4)
    ], className='mb-4'),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='property-count')
        ], width=6),
        dbc.Col([
            dcc.Graph(id='property-features')
        ], width=6)
    ])
], fluid=True, style={'background-color': '#f8f6fa'})


@callback(
    [Output('property-count', 'figure'), Output('property-features', 'figure')],
    [Input('age-dropdown', 'value')]
)
def update_property_count(age_category):
    if age_category in age_categories:
        min_age, max_age = age_categories[age_category]
        filtered_df = df[(df['propertyAge'] >= min_age) & (df['propertyAge'] < max_age)]
        neighborhood_counts = filtered_df['neighbourhood'].value_counts().reset_index()
        neighborhood_counts.columns = ['neighbourhood', 'Count']

        fig1 = px.bar(neighborhood_counts, x='neighbourhood', y='Count',
                      labels={'neighbourhood': 'Neighbourhood', 'Count': 'Count'},
                      title='Property Count by Neighborhood')

        property_feature_counts = filtered_df[property_features].sum()

        fig2 = px.bar(x=property_features, y=property_feature_counts,
                      labels={'x': 'Property Features', 'y': 'Count'},
                      title='Property Features Count')

        fig1.update_layout(
            font=dict(size=12),
            width=600,
            height=400,
            legend=dict(orientation="h", x=0, y=-0.2),
            colorway=['#66c5cc']
        )

        fig2.update_layout(
            font=dict(size=12),
            width=600,
            height=400,
            legend=dict(orientation="h", x=0, y=-0.2),
            colorway=['#f6cf71']
        )

        # Apply color palette
        fig1.update_traces(marker_color='#66c5cc')
        fig2.update_traces(marker_color='#f6cf71')

        return fig1, fig2

    return None, None
