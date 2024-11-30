from dash import dcc
import plotly.express as px

def create_graph(data, column, title):
    if column == "Sector":
        return px.bar(data, x=column, title=title)
    elif column == "Industria":
        return px.pie(data, names=column, title=title)

