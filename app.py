from dash import Dash
import dash_bootstrap_components as dbc
from layouts.datos_layout import layout  # Importar el layout desde datos_layout

# Inicialización de la aplicación
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,  # Para evitar errores si hay callbacks en otras partes no cargadas aún
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}]  # Responsividad
)

# Asegurarse de que el servidor sea accesible para Gunicorn
server = app.server

# Configuración del layout principal
app.layout = layout

# Importar los callbacks
# Esto asume que `datos_callbacks` registra los callbacks con la aplicación `app`.
try:
    import callbacks.datos_callbacks
except ImportError as e:
    print(f"Error al importar los callbacks: {e}")

# Ejecutar la aplicación localmente
if __name__ == "__main__":
    app.run_server(debug=True)
