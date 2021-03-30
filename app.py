### Data
import pandas as pd
import pickle
### Graphing
import plotly.graph_objects as go
### Dash
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
## Navbar
from navbar import Navbar



nav = Navbar()

def App ():
    layout = html.Div ([
        nav,
        header,
        dropdown,
        output
    ])
    return layout



def build_graph (city):
    data = [go.Scatter (x = df.index,
                            y = df [city],
                            marker = {'color': 'orange'})]
    graph = dcc.Graph (
               figure = {
                   'data ': data,
    ' layout ': go.Layout (
                        title =' {} Population Change'.format (city),
                        yaxis = {'title': 'Population'},
                        hovermode = 'narrow'
                                      )
                           }
                 )
    return graph
