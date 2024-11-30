from dash import Input, Output, callback
import pandas as pd
from dash import html

# Carga de datos
data_path = "./data/outputs/tickers.csv"
tickers_data = pd.read_csv(data_path)

@callback(
    [Output("sector-filter", "options"),
     Output("sector-filter", "value"),  
     Output("sector-graph", "figure"),
     Output("industry-table", "children")],
    Input("sector-filter", "value")
)
def update_content(selected_sector):
    # Opciones para el filtro de sector
    sector_options = [{"label": sector, "value": sector} for sector in tickers_data['Sector'].unique()]
    default_value = "Basic Materials" 

    # Conteo de acciones por sector
    sector_counts = tickers_data.groupby('Sector')['Ticker'].count().reset_index()
    sector_counts.columns = ['Sector', 'Número de Acciones']
    sector_counts = sector_counts.sort_values(by='Número de Acciones', ascending=False)

    # Gráfico de sectores
    sector_fig = {
    'data': [
        {
            'x': sector_counts['Sector'],
            'y': sector_counts['Número de Acciones'],
            'type': 'bar',
            'text': sector_counts['Número de Acciones'],  
            'textposition': 'inside',  
            'marker': {'color': '#064469'}
        }
    ],
    'layout': {
        'title': {
            'text': 'Número de Acciones por Sector',
            'y': 0.95,  # Ajustar la posición vertical del título
            'x': 0.5,  # Centrar el título
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 18}  
        },
        'xaxis': {
            'title': {
                'text': 'Sector',  # Título del eje X
                'standoff': 40  # Distancia entre etiquetas y título del eje X
            },
            'tickangle': 90,  # Girar las etiquetas del eje X 90 grados
            'automargin': True  # Ajustar automáticamente los márgenes
        },
        'yaxis': {
            'title': 'Número de Acciones',
            'automargin': True  # Ajustar automáticamente los márgenes
        },
        'template': 'plotly_white',
        'margin': {
            't': 100,  # Espacio superior para el título
            'b': 150,  # Espacio inferior para las etiquetas del eje X
            'l': 50,  # Espacio izquierdo
            'r': 50   # Espacio derecho
        }
    }
}

    # Filtrado y tabla de industrias
    if not selected_sector:
        selected_sector = default_value

    filtered_data = tickers_data[tickers_data['Sector'] == selected_sector]
    industry_counts = filtered_data.groupby('Industria')['Ticker'].count().reset_index()
    industry_counts.columns = ['Industria', 'Acciones en la Industria']
    industry_counts = industry_counts.sort_values(by='Acciones en la Industria', ascending=False)

    # Construcción de la tabla
    table_header = [
        html.Thead(html.Tr([html.Th("Industria"), html.Th("Acciones en la Industria")]))
    ]
    table_body = [
        html.Tbody([
            html.Tr([html.Td(row['Industria']), html.Td(row['Acciones en la Industria'])])
            for _, row in industry_counts.iterrows()
        ])
    ]

    return sector_options, default_value, sector_fig, table_header + table_body
