 
from dash import html

def create_navbar():
    return html.Nav([
        html.Div("Dashboard: Optimización de Portafolios", className="navbar-brand"),
        html.Ul([
            html.Li(html.A("Datos", href="/datos"), className="nav-item"),
            html.Li(html.A("EDA", href="/eda"), className="nav-item"),
            html.Li(html.A("Riesgos", href="/riesgos"), className="nav-item"),
            html.Li(html.A("Optimización", href="/optimizacion"), className="nav-item"),
            html.Li(html.A("Benchmark", href="/benchmark"), className="nav-item"),
            html.Li(html.A("Implementación", href="/implementacion"), className="nav-item"),
        ], className="navbar-nav")
    ], className="navbar navbar-expand-lg navbar-dark bg-primary")
