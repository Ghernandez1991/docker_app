from dash import Dash, dcc, html
import pandas as pd
from pathlib import Path


def create_dash_app(flask_server):
    """
    Create a Dash app and attach it to the Flask server.
    """
    dash_app = Dash(
        __name__, server=flask_server, url_base_pathname="/dashboard/"
    )  # noqa

    pie_chart_dictionary = get_pie_chart_data()

    # Dash layout with a static pie chart
    dash_app.layout = html.Div(
        [
            html.H1("Offender Last Statements", style={"textAlign": "center"}),
            dcc.Graph(
                id="Most Common File Words",
                figure={
                    "data": [
                        {
                            "type": "pie",
                            "labels": list(
                                pie_chart_dictionary.get("Most_Spoken_Words")
                            ),  # noqa
                            "values": list(
                                pie_chart_dictionary.get("Count_of_Words")
                            ),  # noqa
                            "textinfo": "label+percent",
                            "textposition": "inside",
                        }
                    ],
                    "layout": {
                        "title": {"text": "Most Common Final Words", "x": 0.5},
                        "height": 600,
                        "width": 800,
                    },
                },
            ),
        ]
    )

    return dash_app


def get_pie_chart_data():

    db_path = Path("/app/data/executions.sqlite")
    full_db_path = f"sqlite:///{db_path}"
    words_df = pd.read_sql_table("words", full_db_path)

    list_of_words = words_df["Most_Spoken_Words"].to_list()
    count_of_words = words_df["Count_of_Words"].to_list()

    words_dictionary = {
        "Most_Spoken_Words": list_of_words,
        "Count_of_Words": count_of_words,
    }

    return words_dictionary


def create_links():

    db_path = Path("/app/data/executions.sqlite")
    full_db_path = f"sqlite:///{db_path}"
    offenders = pd.read_sql_table("offender", full_db_path)

    last_names = offenders["Last_Name"].to_list()
    first_names = offenders["First_Name"].to_list()

    len(last_names)
    len(first_names)
    zipped = zip(last_names, first_names)

    last_statement_list = []
    for item in zipped:
        last_name = item[0].split(",", 1)[0]
        first_name = item[1]
        base_url = f"https://www.tdcj.texas.gov/death_row/dr_info/{last_name}{first_name}last.html"  # noqa
        last_statement_list.append(base_url)

    return last_statement_list
