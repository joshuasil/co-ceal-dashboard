import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output
import dash
import pandas as pd
from custom_functions.custom_functions import *
import os
from dotenv import load_dotenv
import plotly.express as px
load_dotenv()


wave2_df = pd.read_excel("data/wave_2.xlsx",engine='openpyxl')

displayModeBar_str = os.environ.get("displayModeBar", "True")
displayModeBar = displayModeBar_str.lower() == "true"
displaylogo_str = os.environ.get("displaylogo", "True")
displaylogo = displaylogo_str.lower() == "true"




wave_2_title = html.Div([
    html.H1("Welcome to Your Dashboard for Wave 2", className="my-custom-title text-center"),
])

wave_2_age_histogram = create_histogram(wave2_df, 'Age', title_text="Age Distribution", num_bins=15)
wave_2_lang_pie_chart = create_pie_chart(wave2_df, 'Language', 'counter_column', 'Survey Language Distribution')
wave_2_community_icicle_chart = create_icicle_chart(wave2_df,'Are you Hispanic or Latino? ','Community', 'counter_column', "Community Ethnicity Chart")
wave_2_gender_bar_chart = create_horizontal_bar_chart(wave2_df, 'Gender', 'Gender')

wave_2_testing_bar_chart = covid_testing_bar_chart(wave2_df, 'COVID Testing Behaviour')
wave_2_flu_vacaine_bar_chart = flu_vaccine_bar_chart(wave2_df, 'Flu Vaccine Behaviour')
trust_by_community_bar_chart = trust_by_community(wave2_df, 'Average Trust by Community')
wave_2_vaccine_bar_chart = covid_vaccine_bar_chart(wave2_df, 'COVID Vaccination Behaviour')

wave_2_demographic_figures = html.Div([
            html.Div([
                dcc.Graph(id="wave-2-age-histogram", className="figure",figure=wave_2_age_histogram,
                          config={"displayModeBar": True, "displaylogo": displayModeBar},),
                dcc.Graph(id="wave-2-lang-pie-chart", className="figure",figure=wave_2_lang_pie_chart,
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},),
                ], className="row-container"),
            html.Div([
                dcc.Graph(id="wave-2-community-icicle-chart", className="figure", figure = wave_2_community_icicle_chart,
                          config={"displayModeBar": True, "displaylogo": displayModeBar},),
                dcc.Graph(id="wave-2-gender-bar-chart", className="figure", figure = wave_2_gender_bar_chart,
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},),
                ], className="row-container"),
        ])

wave_2_tab2_figures = html.Div([
            html.Div([
                dcc.Graph(id="wave-2-testing-bar-chart", className="figure",
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},
                        figure=wave_2_testing_bar_chart,),
                dcc.Graph(id="trust-by-community-bar-chart", className="figure",
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},
                        figure=trust_by_community_bar_chart),
                ], className="row-container"),
            html.Div([
                dcc.Graph(id="wave-2-flu-vaccine-bar-chart", className="figure",
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},
                        figure=wave_2_flu_vacaine_bar_chart),
                dcc.Graph(id="wave-2-vaccine-bar-chart", className="figure",
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},
                        figure=wave_2_vaccine_bar_chart),
                ], className="row-container"),
        ])

wave_2_tab3_figures = html.Div([
            html.Div([
                dcc.Graph(id="figure-3", className="figure",
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},
                        figure=get_figure_layout("wave 2 tab 3 fig 1"),),
                dcc.Graph(id="figure-4", className="figure",
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},
                        figure=get_figure_layout("wave 2 tab 3 fig 2"),),
                ], className="row-container"),
            html.Div([
                dcc.Graph(id="figure-3", className="figure",
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},
                        figure=get_figure_layout("wave 2 tab 3 fig 3"),),
                dcc.Graph(id="figure-4", className="figure",
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},
                        figure=get_figure_layout("wave 2 tab 3 fig 4"),),
                ], className="row-container"),
        ])


wave_2_figure_groups = {
    "wave-2-demographics-tab" : wave_2_demographic_figures,
    "tab-2" : wave_2_tab2_figures,
    "tab-3" : wave_2_tab3_figures,
}

wave_2_tabs = html.Div(
    [
        dbc.Tabs([
            dbc.Tab(label="Demographics", id="wave-2-demographics-tab", className="nav-item",
                    active_tab_style={"textTransform": "uppercase"}, active_label_style={"color": "#FB79B3"}, active_tab_class_name="fw-bold fst-italic", activeLabelClassName="text-success"),
            dbc.Tab(label="Vaccine Behaviour", id="tab-2", className="nav-item",
                    active_tab_style={"textTransform": "uppercase"}, active_label_style={"color": "#FB79B3"}, active_tab_class_name="fw-bold fst-italic", activeLabelClassName="text-success"),
            dbc.Tab(label="Tab 3", id="tab-3", className="nav-item",
                    active_tab_style={"textTransform": "uppercase"}, active_label_style={"color": "#FB79B3"}, active_tab_class_name="fw-bold fst-italic", activeLabelClassName="text-success"),
        ],
            id="wave-2-tabs",
            active_tab="wave-2-demographics-tab",
            className="nav-fill justify-content-center",
        ),
        html.Div(id="wave-2-content"),
    ]
)

#active_tab_style={"textTransform": "uppercase"}, active_label_style={"color": "#FB79B3"}, active_tab_class_name="fw-bold fst-italic", activeLabelClassName="text-success")