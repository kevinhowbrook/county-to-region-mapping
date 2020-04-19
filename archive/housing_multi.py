import pandas as pd

from utils import region

"""Housing stock multi
The data files for this are split 09 > 12 but the end result should be the
same, see the expected structure in the /data
"""


# First add a year variable to the data depending on what file we are using
# and munge all the data to one frame
file_name_range = list(range(2009, 2019))
print(file_name_range)
master_df = pd.DataFrame()
for i in file_name_range:
    i = str(i)
    file_name = f"data/edited/housing_stock_2009_onwards_la_{i}.csv"
    df = pd.read_csv(file_name, thousands=",")
    # Iterate through the rows in the Df and for each row, fill in the region
    # as a new variable depending on the county.
    df["year"] = i
    master_df = master_df.append(df)

master_df.to_csv("output/tmp/housing_multi.csv")
# Impute the region data
out = region.impute_region("output/tmp/housing_multi.csv", "local_authority", 1)
mask = out.region == "East of England"
column_name = "region"
out.loc[mask, column_name] = "South East"

out.to_csv("output/tmp/housing_multi_region_added.csv")
out.to_csv("output/final_data_files/regions/housing_multi.csv")

# TODO parse out UA


""" Sanitize """
# Get rid of anything without a region
# out = out.drop(out[out.region == "0"].index)
# format null data and nan
out["local_authority_stock"] = out["local_authority_stock"].replace([".."], "0")
out["local_authority_stock"] = out["local_authority_stock"].replace(["--"], "0")
out["local_authority_stock"] = out["local_authority_stock"].replace(["-"], "0")
out["local_authority_stock"] = out["local_authority_stock"].replace(["."], "0")
try:
    out["local_authority_stock"] = (
        out["local_authority_stock"].str.replace(",", "").astype(float)
    )
except AttributeError:
    pass
out["housing_association_stock"] = out["housing_association_stock"].replace([".."], "0")
out["housing_association_stock"] = out["housing_association_stock"].replace(["--"], "0")
out["housing_association_stock"] = out["housing_association_stock"].replace(["-"], "0")
out["housing_association_stock"] = out["housing_association_stock"].replace(["."], "0")
try:
    out["housing_association_stock"] = (
        out["housing_association_stock"].str.replace(",", "").astype(float)
    )
except AttributeError:
    pass
out["other_ps_stock"] = out["other_ps_stock"].replace([".."], "0")
out["other_ps_stock"] = out["other_ps_stock"].replace(["--"], "0")
out["other_ps_stock"] = out["other_ps_stock"].replace(["-"], "0")
out["other_ps_stock"] = out["other_ps_stock"].replace(["."], "0")
try:
    out["other_ps_stock"] = out["other_ps_stock"].str.replace(",", "").astype(float)
except AttributeError:
    pass
out["private_stock"] = out["private_stock"].replace([".."], "0")
out["private_stock"] = out["private_stock"].replace(["--"], "0")
out["private_stock"] = out["private_stock"].replace(["-"], "0")
out["private_stock"] = out["private_stock"].replace(["."], "0")
try:
    out["private_stock"] = out["private_stock"].str.replace(",", "").astype(float)
except AttributeError:
    pass
out["total"] = out["total"].replace([".."], "0")
out["total"] = out["total"].replace(["--"], "0")
out["total"] = out["total"].replace(["-"], "0")
out["total"] = out["total"].replace(["."], "0")
try:
    out["total"] = out["total"].str.replace(",", "").astype(float)
except AttributeError:
    pass
out.to_csv("output/final_data_files/housing_multi.csv")

# # Group by region and preserve the variable so we can use it for reshaping
# year_range = [str(i) for i in list(range(2009, 2019))]
out = out.groupby(["region", "year"], as_index=False)[
    "local_authority_stock",
    "private_stock",
    "other_ps_stock",
    "housing_association_stock",
    "total",
].sum()
out.to_csv("output/final_data_files/housing_multi.csv")

# # Re-shape
# out = out.melt("region", var_name="year", value_name="Value")
# out = out.sort_values(by=["region", "year"])
# out = out.reset_index(drop=True)
# # out.to_csv("output/final_data_files/housing_multi.csv")
