"""Given a csv, adds region data and returns a dataframe"""

import pandas as pd
import numpy as np

from utils.lookups import county_to_region, geography, local_auth_code_to_county


def impute_region(csv):
    df = pd.read_csv(csv)
    # TODO, turn this into a sanity check before running so different data files can be used
    # First get a list of all the counties in the data and check they exist in the mapping function
    counties = df["Met and Shire Counties"].values.tolist()
    # Remove duplicates from the list of counties, basically all the NaNs
    counties = list(set(counties))

    # Now check all counties are in the utils.mapping list
    # TODO improve this, it's lazy
    # convert all the counties in the geograpy dict to a list for comparing
    # in the date. Make sure we have accounted for all counties having a regions
    geography_list = []
    for r, c in geography.items():
        for i in c:
            geography_list.append(i)

    # Iterate through the rows in the Df and for each row, fill in the region
    # as a new variable depending on the county.
    df["region"] = ""
    for i, row in enumerate(df.itertuples()):  # enumeration means the row begins 0
        # Check this rows county and get it's region and populate the region var
        geo_data = local_auth_code_to_county(df.at[i, "Area code"])
        if geo_data:
            if geo_data["region_name"]:
                df.at[i, "region"] = geo_data["region_name"]
    return df
