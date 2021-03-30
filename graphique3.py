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
# First step, import libraries.
import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt
import datetime
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model,Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import os

dossier = os.listdir('data')


#loading the data.
df = pd.DataFrame()
# for file in dossierBtc: 
#   df=pd.concat([df,pd.read_csv("data/"+file)],axis = 0)
df = pd.read_csv("data/btceur.csv")
df['date'] = pd.to_datetime(df['time'],unit='ms').dt.date
group = df.groupby('date')
Real_Price = group['close'].mean()

Real_Price.tail()

# split data
prediction_days = 30
df_train= Real_Price[:len(Real_Price)-prediction_days]
df_test= Real_Price[len(Real_Price)-prediction_days:]

# Data preprocess
training_set = df_train.values
training_set = np.reshape(training_set, (len(training_set), 1))
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler()
training_set = sc.fit_transform(training_set)
X_train = training_set[0:len(training_set)-1]
y_train = training_set[1:len(training_set)]
X_train = np.reshape(X_train, (len(X_train), 1, 1))

# Making the predictions



model = Sequential()
model.add(LSTM(64, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])))
# model.add(BatchNormalization())
model.add(LSTM(32))
model.add(Dense(1))
model.load_weights("bitcoin_model.h5")

# Visualising the results
test_set = df_test.values
inputs = np.reshape(test_set, (len(test_set), 1))
inputs = sc.transform(inputs)
inputs = np.reshape(inputs, (len(inputs), 1, 1))
predicted_BTC_price = model.predict(inputs)
predicted_BTC_price = sc.inverse_transform(predicted_BTC_price)
predicted_BTC_price = [x[0] for x in predicted_BTC_price]
print("************************")
print("\n\n\n Test set: ",test_set)
print("\n\n\n predicted_BTC_price : ", predicted_BTC_price)
print("************************")
dropdown =dbc.Container([

    html.Div([

        html.Div([
            html.H3('Choisir les algorithmes de prédictions'),

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

            # dcc.Graph(id='pret_risque')
            dcc.Graph(
                id='algos',
                figure={
                    'data': [go.Scatter(
                    x=df_test.index,
                    y=test_set,
                    marker={'color':'rgba('+str(random.randint(1,255))+', '+str(random.randint(1,255))+', '+str(random.randint(1,255))+', 0.5)',
                                      'line':{
                                        'color':'rgb('+str(random.randint(1,255))+','+str(random.randint(1,255))+','+str(random.randint(1,255))+')',
                                        'width':0.5,
                                        }
                            }

                ), 
                     
                    go.Scatter(
                    x=df_test.index,
                    y=predicted_BTC_price,
                    marker={'color':'rgba('+str(random.randint(1,255))+', '+str(random.randint(1,255))+', '+str(random.randint(1,255))+', 0.5)',
                                      'line':{
                                        'color':'rgb('+str(random.randint(1,255))+','+str(random.randint(1,255))+','+str(random.randint(1,255))+')',
                                        'width':0.5,
                                        }
                            }

        )    ],


                    'layout': go.Layout(
                        title= "Prédiction des valeurs du bitcoin par rapport à l'euro" ,
                        xaxis={'title': 'Date'},
                        yaxis={'title': "Valeur du Bitcoin "},
                        margin={'l': 40, 'b': 40, 't': 50, 'r': 0},
                        hovermode='closest'
                        )
                } 
            )
        ], className="six columns"),

    ]) ])


def change_dr_risque(crypto_name1,crypto_name2):

    print("je vais renvoyer du coup wina ")
    print("*******************************************")
    print("*******************************************")
    print("*******************************************")
    return {

        'data': [
       
                     
                    go.Scatter(
                    x=df_test.index,
                    y=predicted_BTC_price,
                    marker={'color':'rgba('+str(random.randint(1,255))+', '+str(random.randint(1,255))+', '+str(random.randint(1,255))+', 0.5)',
                                      'line':{
                                        'color':'rgb('+str(random.randint(1,255))+','+str(random.randint(1,255))+','+str(random.randint(1,255))+')',
                                        'width':0.5,
                                        }
                            }

        )    ],


        'layout': go.Layout(
            title= "Prédiction des valeurs du bitcoin par rapport à l'euro" ,
            xaxis={'title': 'Date'},
            yaxis={'title': "Valeur du Bitcoin "},
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
html.Span('Visualisation des prédictions des fluctuations des cryptomonnaies ', style={'color': 'blue'})

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

def build_graph (crypto_name1,crypto_name2):
    callback = change_dr_risque( crypto_name1,crypto_name2)
    return callback
