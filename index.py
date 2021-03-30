import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from graphique1 import App as App1,build_graph as build_graph1
# from graphique2 import App as App2,build_graph as build_graph2
from graphique3 import App as App3,build_graph as build_graph3
# from graphique4 import App as App4
import dash_bootstrap_components as dbc

from homepage import Homepage

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP,'style.css'])

app.config.suppress_callback_exceptions = True

app.layout = html.Div ([
    dcc.Location (id = 'url', refresh = False),
    html.Div (id = 'page-content')
])


@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/Column1':
        return App1()

    #elif pathname == '/Column2':
     #   print("je vais dans la columns 2")
      #  return App2()
    elif pathname == '/Column3':
        return App3()
    #elif pathname == '/Column4':
     #   return App4()

    else:
        return Homepage()

@app.callback(
    Output('pret_risque', 'figure'),
    [Input('risque_dr', 'value'),Input('risque_dr2', 'value')]
)

def change_dr_risque(crypto_name1,crypto_name2):
    print("*******************************************")
    print("*******************************************")
    graph = build_graph3(crypto_name1,crypto_name2)
    return graph

@app.callback(
    Output('objectif_dr', 'figure'),
    [Input('objectif', 'value'),
     Input('dr', 'value')
     ])

def update_graph_dr_objectif(choix_dr,choix_autre_dr):
    graph = build_graph1(choix_dr,choix_autre_dr)
    return graph









if __name__ == '__main__':
    app.run_server(debug=True)
