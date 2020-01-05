"""Given a csv, adds region data and returns a dataframe"""

import pandas as pd
import numpy as np

from utils.lookups import geography, local_string_to_region

"""[summary]

Returns:
    [type] -- [description]
"""


def impute_region(csv, variable_name):
    df = pd.read_csv(csv)
    # Iterate through the rows in the Df and for each row, fill in the region
    # as a new variable depending on the county.
    df["region"] = ""
    for i, row in enumerate(df.itertuples()):  # enumeration means the row begins 0
        # Check this rows county and get it's region and populate the region var
        geo_data = local_string_to_region(df.at[i, variable_name])
        if geo_data:
            if geo_data["region_name"]:
                df.at[i, "region"] = geo_data["region_name"]
        else:
            df.at[i, "region"] = "0"
    return df
