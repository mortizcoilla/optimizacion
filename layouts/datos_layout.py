from dash import dcc, html
import dash_bootstrap_components as dbc
from layouts.intro_section import get_intro_section

def layout():
    data_path = "./data/outputs/tickers.csv"

    return html.Div([
        html.H2("Análisis de Datos", className="mt-4", style={"textAlign": "center"}),

        # Sección de introducción
        get_intro_section(data_path),

        dbc.Container([
            dbc.Row([
                # Columna izquierda con gráfico de sectores
                dbc.Col(
                    dcc.Graph(id="sector-graph"),
                    xs=12, sm=12, md=12, lg=6, xl=6  # Responsividad de las columnas
                ),
                # Columna derecha con filtro y tabla
                dbc.Col([
                    dcc.Dropdown(
                        id="sector-filter",
                        placeholder="Seleccione un sector",
                        style={"marginBottom": "10px"}
                    ),
                    html.Div(
                        id="industry-table-container",
                        children=[
                            html.Table(id="industry-table", className="table table-striped")
                        ],
                        style={"overflowY": "auto", "height": "400px"}
                    )
                ],
                xs=12, sm=12, md=12, lg=6, xl=6
                )
            ], className="mt-4")
        ], fluid=True)
    ], style={
        "paddingLeft": "2%",
        "paddingRight": "2%"  # Espaciado lateral consistente
    })
