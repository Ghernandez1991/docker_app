from dataclasses import dataclass
import pandas as pd
import random
from pathlib import Path


@dataclass
class EndPoints:

    db_path = Path("/app/data/executions.sqlite")
    full_db_path = f"sqlite:///{db_path}"

    def index_method(self):
        offender_df = pd.read_sql_table("offender", EndPoints.full_db_path)

        offender_dictionary = offender_df.to_dict("index")
        random_offender = random.choice(list(offender_dictionary.values()))
        base_url = "https://www.google.com/search"
        first_name = random_offender.get("First_Name")
        last_name = random_offender.get("Last_Name")
        last_name_for_tdcj = last_name.split(",", 1)[0]
        formatted_url = f"{base_url}?q={first_name + " " + last_name + " " + "texas death row"}"  # noqa
        tdcj_link = f"https://www.tdcj.texas.gov/death_row/dr_info/{last_name_for_tdcj}{first_name}last.html"  # noqa
        print(random_offender)
        print(formatted_url)
        print(tdcj_link)
        print(last_name_for_tdcj)
        return (random_offender, formatted_url, tdcj_link, last_name_for_tdcj)
