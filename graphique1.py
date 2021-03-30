### Data
import pandas as pd
import numpy as np
import pickle
### Graphing
import plotly.graph_objects as go
### Dash
import dash
import dash_table
import random
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
## Navbar
from navbar import Navbar
# Importer les lirairies
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
plt.style.use("ggplot")

from datetime import datetime
import os


#Importer les noms de fichiers

dossier = os.listdir('data')

app = dash.Dash( __name__, external_stylesheets=[dbc.themes.BOOTSTRAP,'https://codepen.io/chriddyp/pen/bWLwgP.css'])


# L'import des données


dossier_1 = sorted(list(set([ x[:3] for x in dossier])))
dossier_2 = sorted(list(set([ x[3:6] for x in dossier])))

dropdown =dbc.Container([

    html.Div([

        html.Div([
            html.H3('Choisir les cryptomonnaies'),

            # html.Div([
            #     html.H5("Choisir la fonction de calcul"),
            #     dcc.Dropdown(id='objectif',
            #     options=[{'label': x[:3] +" --> " +x[3:6], 'value': x } for x in dossier],
            #     value='ltcust.csv')
            #          ],
            #           style={'padding':50,'width':'40%','display':'inline-block'}),

            html.Div([
                html.H5("Choisir la première monnaie"),
                dcc.Dropdown(id='objectif',
                options=[{'label': x , 'value': x} for x in ["Aucune sélection"]+dossier_1],
                value=''
                             )
            ], style={'padding':50,'width':'25%','display':'inline-block'}),
            html.Div([
                html.H5("Choisir la seconde monnaie"),
                dcc.Dropdown(id='dr',
                options=[{'label': x, 'value': x} for x in ["Aucune sélection"]+dossier_2],
                value=''
                             )
            ], style={'padding':50,'width':'25%','display':'inline-block'}),

            dcc.Graph(id='objectif_dr')
        ], className="six columns"),

    ]) ])

liste_colonne_valeur=['totale_incoherent_dr','totale_incoherent_dr2']
liste_colonne_ville = ["DR_instruction_x","DR_instruction_y"]

def callback_dr_objectif(choix_dr,choix_autre_dr):

    
    
    liste_df=[]
    
    if(choix_dr !="" and choix_autre_dr!="" and choix_dr != "Aucune sélection" and choix_autre_dr != "Aucune sélection"):
        if(True):
            try:
                data_frame_to = pd.read_csv("data/"+choix_dr+choix_autre_dr+".csv")
                data_frame_to["Date_convert"] = [datetime.fromtimestamp(date/1000) for date in data_frame_to.time]
                data_frame_to_index = data_frame_to.set_index(pd.to_datetime(data_frame_to.Date_convert, unit='ms'))
                del data_frame_to
                data_frame_to = data_frame_to_index.copy()
                del  data_frame_to_index
                data_frame_to = data_frame_to.drop(labels = ["Date_convert","time"],axis=1)
                liste_df.append(data_frame_to)
            except:
                print("No file")        
    elif(choix_dr!=""):
        if(choix_dr != "Aucune sélection"):
            liste_dr = [x for x in dossier if(x[0:3] == choix_dr)]
            if(len(liste_dr)>0):
                for file in liste_dr:
                    try:
                        data_frame_2 = pd.read_csv("data/"+file)

                        data_frame_2["Date_convert"] = [datetime.fromtimestamp(date/1000) for date in data_frame_2.time]
                        data_frame_2_index = data_frame_2.set_index(pd.to_datetime(data_frame_2.Date_convert, unit='ms'))
                        del data_frame_2
                        data_frame_2 = data_frame_2_index.copy()
                        del  data_frame_2_index
                        data_frame_2 = data_frame_2.drop(labels = ["Date_convert","time"],axis=1)
                        liste_df.append(data_frame_2)
                    except:
                        print("No file", file)

        
        else :
            choix_dr = ""
            if(choix_autre_dr != "Aucune sélection"):
                liste_autre_dr = [x for x in dossier if(x[3:6] == choix_autre_dr)]
                if(len(liste_autre_dr)>0):
                    for file in liste_dr:
                        try:
                            data_frame_1 = pd.read_csv("data/"+file)
                            data_frame_1["Date_convert"] = [datetime.fromtimestamp(date/1000) for date in data_frame_1.time]
                            data_frame_1_index = data_frame_1.set_index(pd.to_datetime(data_frame_1.Date_convert, unit='ms'))
                            del data_frame_1
                            data_frame_1 = data_frame_1_index.copy()
                            del  data_frame_1_index
                            data_frame_1 = data_frame_1.drop(labels = ["Date_convert","time"],axis=1)
                            liste_df.append(data_frame_1)
                        except:
                            print("No file",file)
            else :
                choix_autre_dr =""

    else :
        
        if(choix_autre_dr!=""):
            if(choix_autre_dr != "Aucune sélection"):
                liste_autre_dr = [x for x in dossier if(x[3:6] == choix_autre_dr)]
                if(len(liste_autre_dr)>0):
                    for file in liste_autre_dr:
                        try:
                            data_frame_1 = pd.read_csv("data/"+file)
                            data_frame_1["Date_convert"] = [datetime.fromtimestamp(date/1000) for date in data_frame_1.time]
                            data_frame_1_index = data_frame_1.set_index(pd.to_datetime(data_frame_1.Date_convert, unit='ms'))
                            del data_frame_1
                            data_frame_1 = data_frame_1_index.copy()
                            del  data_frame_1_index
                            data_frame_1 = data_frame_1.drop(labels = ["Date_convert","time"],axis=1)
                            liste_df.append(data_frame_1)
                        except :
                            print("No file",file)
            else :
                # # print("ici **********************************")
                choix_autre_dr=""
                if(choix_dr != "Aucune sélection"):
                    liste_dr = [x for x in dossier if(x[0:3] == choix_dr)]
                    if(len(liste_dr)>0):
                        for file in liste_dr:
                            try:
                                data_frame_2 = pd.read_csv("data/"+file)
                                data_frame_2["Date_convert"] = [datetime.fromtimestamp(date/1000) for date in data_frame_2.time]
                                data_frame_2_index = data_frame_2.set_index(pd.to_datetime(data_frame_2.Date_convert, unit='ms'))
                                del data_frame_2
                                data_frame_2 = data_frame_2_index.copy()
                                del  data_frame_2_index
                                data_frame_2 = data_frame_2.drop(labels = ["Date_convert","time"],axis=1)
                                liste_df.append(data_frame_2)
                            except :
                                print("No file",file)
                else :
                    choix_dr =""

    return {

        'data': [

            go.Scatter(
            x=df.index,
            y=df['close'],
            marker={'color':'rgba('+str(random.randint(1,255))+', '+str(random.randint(1,255))+', '+str(random.randint(1,255))+', 0.5)',
                              'line':{
                                'color':'rgb('+str(random.randint(1,255))+','+str(random.randint(1,255))+','+str(random.randint(1,255))+')',
                                'width':0.5,
                                }
                    }

        ) for df in liste_df        
        ],


        'layout': go.Layout(
            title= choix_dr.lower() +" to " +choix_autre_dr.lower() ,
            xaxis={'title': 'Date'},
            yaxis={'title': "Valeur de " + choix_dr.lower() + " par rapport à " +  choix_autre_dr.lower()},
            margin={'l': 40, 'b': 40, 't': 50, 'r': 0},
            hovermode='closest'
        ),

 
    }

css=app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})


nav = Navbar()

header = html.Div([
html.Br(),
html.Br(),

html.H3(
html.Span('Visualisation des données des cryptomonnaies ', style={'color': 'blue'})

),
html.Br(),
html.Br()

],style={'height':'70%','width':'90%', 'margin':25, 'textAlign': 'center'})
output = html.Div (id = 'output',
                children = [],
                )

def App ():
    layout = html.Div ([
        nav,
        header,
        dropdown,
        output
    ])
    return layout

def build_graph ( choix_dr,choix_autre_dr):
    callback = callback_dr_objectif( choix_dr,choix_autre_dr)
    return callback
