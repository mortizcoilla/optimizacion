from dash import Dash
import dash_bootstrap_components as dbc
from layouts.datos_layout import layout  # Importar el layout desde datos_layout

# Inicialización de la aplicación
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  # Esto asegura que Gunicorn pueda encontrar la aplicación WSGI

# Configuración del layout
app.layout = layout

# Importar los callbacks
import callbacks.datos_callbacks  # Asegúrate de que este archivo no tenga errores

# Ejecutar la aplicación localmente
if __name__ == "__main__":
    app.run_server(debug=True)
