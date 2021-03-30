import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import base64

#from navbar import NaVbar

from navbar import Navbar
from navbar import Navbar_midle

nav = Navbar()
nav_midle_graphe1 = Navbar_midle(name = "Pré visualisation des Crytodata",color="#42a5f5",pathname = ['Column1'],barename=['Visualisations'])
nav_midle_graphe2 = Navbar_midle("Machine Learning","#2BBBAD",['Column3'],['Prédictions'])

Dauphine = base64.b64encode(open('./mmto.jpeg', 'rb').read()).decode('ascii')


Histogramme1 = base64.b64encode(open('./courbe22.png', 'rb').read()).decode('ascii')
Histogramme_cluster =base64.b64encode(open('./histogramme_cluster.png', 'rb').read()).decode('ascii')
body = dbc.Container(
    [

        #dbc.Row([


                html.Br(),
                html.A([

                html.Img(
             src='data:image/png;base64,{}'.format(Dauphine),
                 style={
             'height' : '20%',
             'width' : '30%',
             'float' : 'right',
             'position' : 'relative',
             'padding-top' : 0,
             'padding-left' : -100,
         }
         ),],"Lien", href= "/Column1"),
                html.H2("KHELOUAT Imane et MOUALI Katia", style={'color': 'gray'}),

                # html.H2("Akli DERRADJ"),
                html.Br(),
                html.Br(),

                html.Br(),
                html.Br(),
                html.H2("Mémoire de fin d'études :", style={'color': 'blue'}),
                html.H3("Prédiction des cours de cryptomonnaie"),
                html.Br(),
                html.Br(),

               dbc.Col(
                  [
                     html.P(
                         """\
                         Ce dashboard est une application de visualisation nous permettant de visualiser dynamiquement les données de fluctuation de plusieurs cryptomonnaie.

                         Nous pouvons aussi visualiser les algorithmes de Machine Learning et leurs résultats. 
                        
                            """
                           ,style={
                       'height' : '80%',
                       'width' : '150%',
                       'float' : 'center',
                       'position' : 'relative',
                       'padding-top' : 0,
                       'padding-left' : 0,
                   }),



                           #dbc.Button("Plus de détail", color="blue",href ="/Column1"),
                   ],
                  md=7,
               ),
    ])


body1=dbc.Container(
        [

        #dbc.Row([


            html.Br(),
             nav_midle_graphe1,
             html.Br(),

             #])
             ])

body2=dbc.Container(
    [

               ########### COlumns 1
                #   dbc.Row([

    #    dbc.Col([
                          html.A([

                          html.Img(
                                      src='data:image/png;base64,{}'.format(Histogramme1),
                                          style={
                                      'height' : '70%',
                                      'width' : '50%',

                                      'float' : 'left',
                                      'position' : 'relative',
                                      'padding-top' : 0,
                                      'padding-left' : 0,
                                  }
                                  ),],"Lien", href= "/Column1"),
                #],style={'display': 'inline-block'}, md=5,),

                ########Column2
#])
])



body4=dbc.Container(
        [

        #dbc.Row([

html.Br(),
            html.Br(),

html.Br(),
            html.Br(),
html.Br(),
            html.Br(),
html.Br(),
            html.Br(),
html.Br(),
            html.Br(),

            nav_midle_graphe2,

            html.Br(),
            html.Br(),


             #])
])

#]),            ######Columns3

#        dbc.Row([

body5=dbc.Container(


[
    #                   dbc.Col([
                                     html.A([html.Img(
                                                 src='data:image/png;base64,{}'.format(Histogramme_cluster),
                                                     style={
                                                 'height' : '30%',
                                                 'width' : '50%',
                                                 'float' : 'right',
                                                 'position' : 'relative',
                                                 'padding-top' : 0,
                                                 'padding-right' : 0
                                             }
                                    ),],"Dynar algerien", href= "/Column3"),
                        #   ], style={'display': 'inline-block'},md=5,),

])
            ######Columns 4
    #dbc.Row([




#className="mt-4",
#)




def Homepage():
    layout = html.Div([
    html.Div([
    nav,
    body,
    body1,
    body2,
    #body3
    #]),
    #html.Div([
    body4,
    body5,
  #  body6
    # html.H1("Contact :"),
    ]),
    html.Div([
        html.Br(),
        html.Br(),
        html.Br(),
       # html.H4("Github: https://github.com/achrafbouzekri/Dataviz_dash_IASD"),
    ])
    ])
    return layout



app = dash.Dash(__name__, external_stylesheets = [dbc.themes.UNITED])
app.layout = Homepage()


if __name__ == "__main__":
    app.run_server()
