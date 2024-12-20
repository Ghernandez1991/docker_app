from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from pathlib import Path
from dash_app.dash_app import create_dash_app, create_links
import os
import sqlite3


server = Flask(__name__)

# Integrate Dash app with Flask
create_dash_app(server)

db_path = Path("/app/data/executions.sqlite")
full_db_path = f"sqlite:///{db_path}"

server.config["SQLALCHEMY_DATABASE_URI"] = full_db_path
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(server)


# Flask route for the homepage
@server.route("/")
def index():
    import random

    offender_df = pd.read_sql_table("offender", full_db_path)

    offender_dictionary = offender_df.to_dict("index")
    random_offender = random.choice(list(offender_dictionary.values()))
    base_url = "https://www.google.com/search"
    first_name = random_offender.get("First_Name")
    last_name = random_offender.get("Last_Name")
    last_name_for_tdcj = last_name.split(",", 1)[0]
    formatted_url = (
        f"{base_url}?q={first_name + " " + last_name + " " + "texas death row"}"  # noqa
    )
    tdcj_link = f"https://www.tdcj.texas.gov/death_row/dr_info/{last_name_for_tdcj}{first_name}last.html"  # noqa
    # ep = EndPoints()
    # tdcj_link, random_offender, formatted_url, last_name_for_tdcj = ep.index_method() # noqa

    return render_template(
        "index.html",
        random_offender=random_offender,
        formatted_url=formatted_url,
        tdcj_link=tdcj_link,
        last_name_for_tdcj=last_name_for_tdcj,  # noqa
    )


@server.route("/words")
def words():

    words_df = pd.read_sql_table("words", full_db_path)

    # words_df.head()

    list_of_words = words_df["Most_Spoken_Words"].to_list()
    count_of_words = words_df["Count_of_Words"].to_list()
    words_dictionary = {}
    for i, value in enumerate(list_of_words):
        words_dictionary[i] = {value: count_of_words[i]}

    return jsonify(words_dictionary)


@server.route("/county")
def county():
    county_df = pd.read_sql_table("county", full_db_path)
    county_df = county_df.drop(["index"], axis=1)

    county_dictionary = county_df.to_dict("records")

    return jsonify(county_dictionary)


@server.route("/offenders")
def offenders():

    offender_df = pd.read_sql_table("offender", full_db_path)

    offender_dictionary = offender_df.to_dict("index")

    return jsonify(offender_dictionary)


@server.route("/final_statements")
def final_statements():
    list_of_statements = create_links()

    return jsonify(list_of_statements)


@server.route("/racial_percentages")
def racial_percentages():
    with open("/app/sql/percentage.sql") as file:
        query = file.read()

    # Connect to the SQLite database
    conn = sqlite3.connect("/app/data/executions.sqlite")

    # Create a cursor object
    cursor = conn.cursor()

    # Execute the query
    cursor.execute(query)

    results = cursor.fetchall()

    list_of_dicts = []
    for row in results:
        dictionary_row = {
            "Race": row[0],
            "Total_Executions": row[1],
            "Percentage": row[2],
        }
        list_of_dicts.append(dictionary_row)
    return jsonify(list_of_dicts)


if __name__ == "__main__":
    # use this for local dev
    # host="0.0.0.0", port=8080, debug=True
    # use this for heroku.
    # It will dynamically assign a port using the port env var
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8050)))
