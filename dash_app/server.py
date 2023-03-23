import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc



df = pd.read_csv("data/master.csv")

year_range = [i for i in range(df.year.min(), df.year.max()+1)]
age_group = df.age.unique().tolist()

# App initialization
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])


# filter column:
filter_panel = [
    html.Br(),
    dbc.Row(
        [
            html.H3("World-wide suicide information", style={"marginLeft": 10}),
        ]
    ),
    html.Br(),
    html.Br(),
    dbc.Card(
            [
                html.H4(
                    "Total Number of Suicides", className="card-title", style={"marginLeft": 10}
                ),
                html.Div(
                    id="summary", style={"color": "teal", "fontSize": 26, "marginLeft": 80}
                ),
            ],
            style={"width": "20rem"},
            body=True,
            color="light",
            className="mb-2",
        ),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.H4("Filters", style={"marginLeft": 20}),
    dbc.Card(
            [
                html.H6("Years", className="text-dark"),
                html.Div(
                    [
                        dcc.RangeSlider(
                            year_range[0],
                            year_range[-1],
                            1,
                            id="years_slider",
                            marks=None,
                            tooltip={"placement": "bottom", "always_visible": True},
                            value=[year_range[5], year_range[13]],
                            className="p-0",
                            allowCross=False,
                        ),
                    ],
                ),
                html.Br(),
                # Dropdown for sex
                html.H6("Sex", className="text-dark"),
                dcc.Dropdown(
                    id="sex_input",
                    value=["male"],
                    options=["male", "female"],
                    className="dropdown",
                    multi=True,
                ),
            ],
            style={"width": "20rem"},
            body=True,
            color="light",
            className="mb-2",
    ),
]

## plot layout
plot_body = [
    dbc.Row(
        [
            dbc.Col(
                [
                    dcc.Graph(
                        id="bar_plot",
                        style={
                            "border-width": "0",
                            "width": "100%",
                            "height": "300px",
                        },
                    )
                ],
            ),
        ]
    ),
    html.Br(),
    dbc.Row(
        [
            dbc.Col(
                [
                    dcc.Graph(
                        id="bubble_plot",
                        style={
                            "border-width": "0",
                            "width": "100%",
                            "height": "100%",
                        },
                    )
                ],
            ),
        ]
    ),
]


## Page layout
page_layout = html.Div(
    className="page_layout",
    children=[
        dbc.Row([html.Br()]),
        dbc.Row(
            [
                dbc.Col(filter_panel, className="panel", width=3),
                dbc.Col(plot_body, className="body"),
            ]
        ),
    ],
)

# Overall layout
app.layout = html.Div(id="main", className="app", children=page_layout)

@app.callback(
    Output("bar_plot","figure"),
    Input("sex_input", "value"),
    Input("years_slider", "value")
)
def bar_plot(sex, year):
    min_year = year[0]
    max_year = year[1]
    if len(sex) == 2:
        data = df.query("year >= @min_year & year <= @max_year")
    else:
        gender = sex
        data = df.query("year >= @min_year & year <= @max_year & sex == @gender")
    
    bar_plot = px.histogram(data, x='suicides_no', y='generation', title='Suicides Counts with Different Generations')
    bar_plot.update_layout(
        xaxis_title='Suicide Count',
        yaxis_title='Generations'
    )
    return bar_plot


@app.callback(
    Output("bubble_plot","figure"),
    Input("sex_input", "value"),
    Input("years_slider", "value")
)
def bubble_plot(sex, year):
    min_year = year[0]
    max_year = year[1]
    if len(sex) == 2:
        data = df.query("year >= @min_year & year <= @max_year")
    else:
        gender = sex
        data = df.query("year >= @min_year & year <= @max_year & sex == @gender")
    data = data.dropna()
    bubble_plot = px.scatter(data, 
                            x="population",
                            y="suicides_no",
                            color="age", 
                            size="suicides_no",
                            hover_name="year", 
                            log_x=False, 
                            size_max=40,
                            title = 'Population vs Suicides count, along with other information when hovering on bubbles.')
    bubble_plot.update_layout(
        xaxis_title='Population',
        yaxis_title='Suicide Counts'
    )
    
    return bubble_plot


@app.callback(
    Output("summary", "children"),
    Input("sex_input", "value"),
    Input("years_slider", "value"),
)
def summary(sex,year): 
    min_year = year[0]
    max_year = year[1]
    if len(sex) == 2:
        data = df.query("year >= @min_year & year <= @max_year")
    else:
        gender = sex
        data = df.query("year >= @min_year & year <= @max_year & sex == @gender")
    return data.suicides_no.sum()



