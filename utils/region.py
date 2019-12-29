"""Given a csv, adds region data and returns a dataframe"""

import pandas as pd
import numpy as np

from utils.mapping import county_to_region, geography


def impute_region(csv):
    df = pd.read_csv(csv)
    # drop rows that don't have Met and Shire values, because these are summary roes and all we need.
    print(df)
    df['Met and Shire Counties'].replace('', np.nan, inplace=True)
    df.dropna(subset=['Met and Shire Counties'], inplace=True)
    print(df)
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
        region = False
        try:
            if row[4][0] == "E" and type(row[5]) is str:
                region = county_to_region(row[5])
                df.at[i, "region"] = region
        except TypeError:
            continue
    # Now itterate the rows again and assign a region for the relevant missing rows
    return df
