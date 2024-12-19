from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from pathlib import Path

app = Flask(__name__)


db_path = Path("/app/data/executions.sqlite")
full_db_path = f"sqlite:///{db_path}"

app.config["SQLALCHEMY_DATABASE_URI"] = full_db_path
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)


# create Flask Routes
@app.route("/", methods=["GET"])
def pie():
    import random

    offender_df = pd.read_sql_table("offender", full_db_path)

    offender_dictionary = offender_df.to_dict("index")
    random_offender = random.choice(list(offender_dictionary.values()))

    return render_template("pie.html", random_offender=random_offender)


@app.route("/words")
def words():

    words_df = pd.read_sql_table("words", full_db_path)

    # words_df.head()

    list_of_words = words_df["Most_Spoken_Words"].to_list()
    count_of_words = words_df["Count_of_Words"].to_list()

    words_dictionary = {
        "Most_Spoken_Words": list_of_words,
        "Count_of_Words": count_of_words,
    }

    return jsonify(words_dictionary)


@app.route("/county")
def county():
    county_df = pd.read_sql_table("county", full_db_path)
    county_df = county_df.drop(["index"], axis=1)

    county_dictionary = county_df.to_dict("records")

    return jsonify(county_dictionary)


@app.route("/offenders")
def index():

    offender_df = pd.read_sql_table("offender", full_db_path)

    offender_dictionary = offender_df.to_dict("index")

    return jsonify(offender_dictionary)


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8080, debug=True)
