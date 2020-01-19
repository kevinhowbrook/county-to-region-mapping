"""Given a csv, adds region data and returns a dataframe"""
import pandas as pd

from utils.lookups import local_string_to_region


def impute_region(csv, variable_name, map_counties=0):
    """Populates a region to the dataframe for each Local Auth

    Arguments:
        csv -- The data file
        variable_name {string} -- The name of the variable the Local auth
            data is in, this should basically be the column name we
            are searching

    Keyword Arguments:
        map_counties {int} -- If true, an LA that is not mapped will
            try to be mapped as a county
          (default: {0})

    Returns:
        [type] -- [description]
    """
    df = pd.read_csv(csv, thousands=",")
    # Iterate through the rows in the Df and for each row, fill in the region
    # as a new variable depending on the county.
    df["region"] = ""
    for i, row in enumerate(df.itertuples()):  # enumeration means the row begins 0
        # Check this rows county and get it's region and populate the region var
        # Some values will have the string and the code, so separate here, E.G E06000005 : Darlington
        data_var = str(df.at[i, variable_name])
        if " : " in data_var:
            data_var = data_var.split(": ")[1]
        geo_data = local_string_to_region(data_var, map_counties)
        if geo_data:
            if geo_data["region_name"]:
                df.at[i, "region"] = geo_data["region_name"]
        else:
            df.at[i, "region"] = "0"
    return df
