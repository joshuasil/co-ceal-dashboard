import dash
from dash import html, dcc, callback, Input, Output, State, callback_context


from components.wave_2_components import *


dash.register_page(__name__)

layout = html.Div([ 
    wave_2_title,
    wave_2_tabs,


    # invisible block to register ids. need to find a workaround!!!!
    # html.Div(style = {'display':'none'},
    #                      children = [wave_2_figure_groups["wave-2-demographics-tab"]]),
    
])

# @callback(Output("wave-2-content", "children"), [Input("wave-2-tabs", "active_tab")])
# def update_wave_2_tab(selected_tab):
#     print(selected_tab)
#     if selected_tab == "tab-1":
#         return wave_2_figure_groups["tab-2"]
#     elif selected_tab == "tab-2":
#         return wave_2_figure_groups["tab-3"]
#     return wave_2_figure_groups["wave-2-demographics-tab"]


# @callback(
#     [Output('wave-2-age-histogram', 'figure'),
#      Output('wave-2-lang-pie-chart', 'figure'),
#      Output('wave-2-community-icicle-chart', 'figure'),
#      Output('wave-2-gender-bar-chart', 'figure'),],
#     [Input('gender_filter', 'value'),
#     Input('language_filter', 'value'),
#     Input('community_filter', 'value'),
#     Input('income_filter', 'value'),])
# def callback_func(gender_values,language_values,community_values,income_values):
    
#     temp_df = wave2_df[wave2_df["Gender"].isin(gender_values)]
#     temp_df = temp_df[temp_df["Language"].isin(language_values)]
#     temp_df = temp_df[temp_df["Community"].isin(community_values)]
#     temp_df = temp_df[temp_df["Income"].isin(income_values)]
#     wave_2_age_histogram = create_histogram(temp_df, 'Age', title_text="Age Distribution", num_bins=15)
#     wave_2_lang_pie_chart = create_pie_chart(temp_df, 'Language', 'counter_column', 'Survey Language Distribution')
#     wave_2_community_pie_chart = create_icicle_chart(temp_df,'Are you Hispanic or Latino? ','Community', 'counter_column', "Community Ethnicity Chart")
#     wave_2_gender_bar_chart = create_horizontal_bar_chart(temp_df, 'Gender', 'Gender')
#     pathname = [gender_values,language_values,community_values,income_values]
#     return [wave_2_age_histogram,wave_2_lang_pie_chart,wave_2_community_pie_chart,wave_2_gender_bar_chart ]

# @callback(
#     [Output('wave-2-testing-bar-chart', 'figure'),
#      Output('wave-2-flu-vaccine-bar-chart', 'figure'),
#      Output('trust-by-community-bar-chart', 'figure'),],
#     [Input('gender_filter', 'value'),
#     Input('language_filter', 'value'),
#     Input('community_filter', 'value'),
#     Input('income_filter', 'value'),])
# def callback_func(gender_values,language_values,community_values,income_values):
    
#     temp_df = wave2_df[wave2_df["Gender"].isin(gender_values)]
#     temp_df = temp_df[temp_df["Language"].isin(language_values)]
#     temp_df = temp_df[temp_df["Community"].isin(community_values)]
#     temp_df = temp_df[temp_df["Income"].isin(income_values)]
#     wave_2_testing_bar_chart = covid_testing_bar_chart(temp_df, 'COVID Testing Behaviour')
#     wave_2_flu_vacaine_bar_chart = flu_vaccine_bar_chart(temp_df, 'Flu Vaccine Behaviour')
#     trust_by_community_bar_chart = trust_by_community(temp_df, "Average Trust by Community")
#     pathname = [gender_values,language_values,community_values,income_values]
#     return [wave_2_testing_bar_chart,wave_2_flu_vacaine_bar_chart,trust_by_community_bar_chart]

# @callback(
# [Output('gender_filter', 'value'),
#  Output('language_filter', 'value'),
#  Output('community_filter', 'value'),
#  Output('income_filter', 'value'),],
# [Input('select_all_genders', 'n_clicks'),
#  Input('select_all_languages', 'n_clicks'),
#  Input('select_all_community', 'n_clicks'),
#  Input('select_all_income', 'n_clicks'),],
# [State('gender_filter', 'options'),
#  State('language_filter', 'options'),
#  State('community_filter', 'options'),
#  State('income_filter', 'options'),])

# def update_filters_select_unselect_all(btn1,btn2,btn3,btn4,feature_options_gender,feature_options_language,feature_options_community,feature_options_income):
#     ctx = callback_context
#     input_id = ctx.triggered[0]["prop_id"].split(".")[0]
#     print(input_id)
#     gender_select_all = [i['value'] for i in feature_options_gender]
#     language_select_all = [i['value'] for i in feature_options_language]
#     community_select_all = [i['value'] for i in feature_options_community]
#     income_select_all = [i['value'] for i in feature_options_income]
#     if input_id == 'select_all_genders':

#         if btn1 % 2 != 0: ## Clear all options on even clicks
#             gender_select_all = []
#             #return []
#         else: ## Select all options on odd clicks
#             gender_select_all = [i['value'] for i in feature_options_gender]
#     elif input_id == 'select_all_languages':

#         if btn2 % 2 != 0: ## Clear all options on even clicks
#             language_select_all = []
#             #return []
#         else: ## Select all options on odd clicks
#             language_select_all = [i['value'] for i in feature_options_language]
#     elif input_id == 'select_all_community':

#         if btn3 % 2 != 0: ## Clear all options on even clicks
#             community_select_all = []
#             #return []
#         else: ## Select all options on odd clicks
#             community_select_all = [i['value'] for i in feature_options_community]
#     elif input_id == 'select_all_income':

#         if btn4 % 2 != 0: ## Clear all options on even clicks
#             income_select_all = []
#             #return []
#         else: ## Select all options on odd clicks
#             income_select_all = [i['value'] for i in feature_options_income]

#     return [gender_select_all,language_select_all,community_select_all,income_select_all]


# @callback(
#     [Output('trust-by-community-bar-chart', 'figure',allow_duplicate=True),],

#     [Input('trust-by-community-bar-chart', 'clickData'),],
#     prevent_initial_call=True
# )

# def drilldown(click_data):
#     ctx = dash.callback_context
#     trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
#     print(trigger_id)
#     if trigger_id == 'trust-by-community-bar-chart':
        
#         if click_data is not None:
#             click_data = click_data['points'][0]['label']
#             print(click_data)
#             if click_data not in wave2_df['Community'].unique():
#                 fig = trust_by_community(wave2_df, "Average Trust by Community")
#                 return [fig]
#             temp_df = wave2_df[wave2_df["Community"]==click_data]
#             fig = trust_by_category(temp_df,"Average Trust for "+click_data)
#             return [fig]
#     else:
#         fig = trust_by_community(wave2_df, "Average Trust by Community")
#     return [fig]