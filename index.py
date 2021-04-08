# -*- coding: utf-8 -*-

from app import app
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from layouts import antenne,emetteur,station,support
from callbacks.antenne import *

pages = ["Antenne","Emetteur","Station","Support"]

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink(i, href="/"+i.lower()))
        for i in pages
    ],
    brand="ANFR - Dataviz",
    brand_href="#",
    color="primary",
    dark=True,
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])



@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/antenne':
         return antenne.layout
    if pathname == '/':
        return antenne.layout
    elif pathname == '/emetteur':
         return emetteur.layout

    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)
