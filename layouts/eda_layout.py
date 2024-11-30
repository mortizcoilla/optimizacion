from dash import html, dcc

def create_eda_layout():
    return html.Div([
        html.H2("Análisis Exploratorio de Datos", style={"textAlign": "center"}),
        dcc.Graph(id="histogram-graph"),
        dcc.Graph(id="correlation-matrix")
    ])

