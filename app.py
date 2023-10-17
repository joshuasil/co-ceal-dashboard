import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output

from components.wave_1_components import *
from components.navbar import *
from components.filters import *

from dotenv import load_dotenv
import os

load_dotenv()

# Use the 'LUX' theme from Bootstrap for a clean, mobile-friendly design
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])


# filter_options = html.Div([
#     html.Div([
#         html.Label("Filter 1"),
#         dcc.Dropdown(
#             id="filter-1",
#             options=[
#                 {"label": "Option 1", "value": "option-1"},
#                 {"label": "Option 2", "value": "option-2"},
#                 {"label": "Option 3", "value": "option-3"},
#                 {"label": "Select All", "value": "select-all"},
#             ],
#             multi=True,
#         ),
#     ], className="filter"),
    
#     html.Div([
#         html.Label("Filter 2"),
#         dcc.Dropdown(
#             id="filter-2",
#             options=[
#                 {"label": "Option 1", "value": "option-1"},
#                 {"label": "Option 2", "value": "option-2"},
#                 {"label": "Option 3", "value": "option-3"},
#                 {"label": "Select All", "value": "select-all"},
#             ],
#             multi=True,
#         ),
#     ], className="filter"),
    
#     html.Div([
#         html.Label("Filter 3"),
#         dcc.Dropdown(
#             id="filter-3",
#             options=[
#                 {"label": "Option 1", "value": "option-1"},
#                 {"label": "Option 2", "value": "option-2"},
#                 {"label": "Option 3", "value": "option-3"},
#                 {"label": "Select All", "value": "select-all"},
#             ],
#             multi=True,
#         ),
#     ], className="filter"),
    
#     html.Div([
#         html.Label("Filter 4"),
#         dcc.Dropdown(
#             id="filter-4",
#             options=[
#                 {"label": "Option 1", "value": "option-1"},
#                 {"label": "Option 2", "value": "option-2"},
#                 {"label": "Option 3", "value": "option-3"},
#                 {"label": "Select All", "value": "select-all"},
#             ],
#             multi=True,
#         ),
#     ], className="filter"),
# ], className="filter-container")


app.layout = html.Div([
    html.Link(
        rel='stylesheet',
        href='/assets/custom.css'  # Path to your custom CSS file
        ),
    html.Script(
        src='/assets/script.js'  # Path to your JavaScript file
    ),  
    Navbar,
    wave_1_title,
    filter_options,
    wave_1_tabs,
])


@app.callback(Output("wave-1-content", "children"), [Input("wave-1-tabs", "active_tab")])
def update_wave_1_tab(selected_tab):
    print(selected_tab)
    if selected_tab == "tab-1":
        return wave_1_figure_groups["tab-2"]
    elif selected_tab == "tab-2":
        return wave_1_figure_groups["tab-3"]
    return wave_1_figure_groups["wave-1-demographics-tab"]

if __name__ == '__main__':
    app.run_server(debug=True)
