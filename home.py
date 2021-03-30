import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
        html.Div([
            html.H3('Column 1'),

            html.Div([
                html.H5("Définir l'objectif"),
                dcc.Dropdown(id='objectif',
                options=[{'label': i.title(), 'value': i} for i in ['Totale des prêts non garantis', 'Nombre moyen des Pjs de diff % au min', 'Total des prêts non coherents', 'Total des prêts sans LVR']],
                value='Totale des prêts non garantis')
                     ],
                      style={'padding':50,'width':'50%','display':'inline-block'}),


            html.Form
            html.Div([
                html.H5("définir la DR"),
                dcc.Dropdown(id='dr',
                options=[{'label': i.title(), 'value': i} for i in ["dyna","baghla","tabahant","tayiba"]],
                value='idf'
                             )
            ], style={'width':'30%','display':'inline-block'}),

            dcc.Graph(id='objectif_dr')
        ], className="six columns")])

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

# Add the server clause:
if __name__ == '__main__':
    app.run_server()
