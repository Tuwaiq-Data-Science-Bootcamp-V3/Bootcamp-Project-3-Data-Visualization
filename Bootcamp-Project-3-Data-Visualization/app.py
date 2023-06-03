from dash import Dash, html, dcc
import dash
import dash_bootstrap_components as dbc
from jupyter_dash import JupyterDash

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SKETCHY]) #BOOTSTRAP CERULEAN FLATLY LUMEN SLATE SKETCHY

navbar = dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Pages", header=True),
                html.Div(
                    [
                        html.Div(
                            dbc.DropdownMenuItem(
                                f"{page['name']}", href=page["relative_path"]
                            )
                        )
                        for page in dash.page_registry.values()
                    ]
                ),
            ],
            nav=True,
            in_navbar=True,
            label="Dashboards",
        ),
    ],
    brand="Riyadh Villas Aqar Analysis",
    brand_href="#",
    color="primary",
    dark=True,
)

app.layout = html.Div([
    navbar,
    html.Br(),
    dash.page_container
])


if __name__ == '__main__':
    app.run_server(debug=True)