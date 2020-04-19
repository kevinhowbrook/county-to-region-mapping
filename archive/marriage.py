from utils import region

"""
Run the region logic to populate the region value.
"""
out = region.impute_region(
    "data/edited/la_to_region_marriage_total_2001_2016_edited.csv",
    "local_authority",
    map_counties=1,
)

# out = region.impute_region('tests/test_data.csv')
""" Sanitize """

# Some numerical values are -- so replace these
year_range = [str(i) for i in list(range(2001, 2017))]
for i in year_range:
    out[i] = out[i].replace([".."], "0")
    out[i] = out[i].replace(["-"], "0")


# Get rid of anything without a region
# out = out.drop(out[out.region == ""].index)
# out = out.drop(out[out.region == "0"].index)


mask = out.region == "East of England"
column_name = "region"
out.loc[mask, column_name] = "South East"

# Group by region and preserve the variable so we can use it for reshaping
# out = out.groupby(["region"], as_index=False)[year_range].sum()
# Group by region and preserve the variable so we can use it for reshaping
year_range = [str(i) for i in list(range(2001, 2017))]

# replace string values with floats... for some reason this is missed in the
# read_csv method
for i in year_range:
    try:
        out[i] = out[i].str.replace(",", "").astype(float)
    except AttributeError:
        print(i)
        pass
out.to_csv("output/final_data_files/regions/marriage.csv")

out = out.groupby(["region"], as_index=False)[year_range].sum()
out.to_csv("output/tmp/marriage.csv")

# Re-shape
out = out.melt("region", var_name="Year", value_name="marriages")
out = out.sort_values(by=["region", "Year"])
out = out.reset_index(drop=True)
out.to_csv("output/final_data_files/marriage.csv")
