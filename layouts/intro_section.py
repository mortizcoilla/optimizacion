from dash import html
import pandas as pd

# Función para generar la introducción
def get_intro_section(data_path):
    # Cargar los datos
    tickers_data = pd.read_csv(data_path)

    # Calcular X (número de acciones) y Y (sectores principales)
    num_acciones = len(tickers_data)
    sectores_principales = ', '.join(tickers_data['Sector'].value_counts().head(3).index)  # Top 3 sectores

    # Texto introductorio
    texto = f"""
    Este estudio analiza un conjunto de {num_acciones} acciones transadas en la Bolsa de Santiago, con el objetivo de identificar oportunidades de inversión y optimizar portafolios. Los datos permiten comprender la composición y comportamiento de los principales sectores económicos, destacando {sectores_principales} como los más relevantes.

    La optimización de carteras busca maximizar el retorno esperado para un nivel de riesgo definido, utilizando métodos como la diversificación sectorial y el análisis de rentabilidad y riesgo. Para ello, se aplicará el modelo de Markowitz, que identifica combinaciones óptimas de activos para construir portafolios eficientes.
    """

    # Crear componente HTML sin márgenes laterales
    return html.Div(
        html.P(texto, style={
            "textAlign": "center",
            "margin": "50px auto",  # Margen superior/inferior
            "padding": "0 10px",  # Incrementar el espacio lateral
            "fontSize": "16px",
            "maxWidth": "900px",  # Limitar el ancho máximo del texto
            "lineHeight": "1.6",
        }),
        style={
            "display": "flex",
            "justifyContent": "center"
        }
    )
