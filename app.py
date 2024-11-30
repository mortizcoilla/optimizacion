from dash import Dash
import dash_bootstrap_components as dbc
from layouts.datos_layout import layout as datos_layout

# Inicialización de la aplicación
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Configuración del layout (sin invocar como función)
app.layout = datos_layout

# Registrar los callbacks
from callbacks.datos_callbacks import update_content

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run_server(debug=True)
