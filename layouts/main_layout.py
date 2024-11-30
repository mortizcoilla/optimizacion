 
from dash import html

def create_main_layout():
    return html.Div([
        html.H1("Dashboard de Optimización de Portafolios", style={"textAlign": "center"}),
        html.P("Seleccione una sección en la barra de navegación para empezar.")
    ])
