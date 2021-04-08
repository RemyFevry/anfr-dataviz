from dash.dependencies import Input, Output
import pandas as pd
from app import app

d_antenne=pd.read_csv("data/DELTA_ANTENNE.csv",
                        encoding="latin-1",
                        low_memory=False,
                        index_col=0)

@app.callback(
    Output('app-1-display-value', 'children'),
    Input('app-1-dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)


@app.callback(
    Output('app-2-display-value', 'children'),
    Input('app-2-dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)
