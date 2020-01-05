import glob
import pandas as pd
from utils import region


""" Loop over all the data files and populate region data
and make a list of dataframes to merge """
# TODO when we have more data and if possible
# data_frames = []
# for i, f in enumerate(glob.glob("data/*.csv")):
#     data_frames.append(region.impute_region(f))

# new_df = []
# for d in data_frames:
#     for i, row in enumerate(d.itertuples()):  # enumeration means the row begins 0
#         print(row)
#         new_df.append(row)

# out = pd.DataFrame(new_df)

""" Merge all the new data to one data set on Year and Region """
# TODO - this will be an append
# new_df = pd.merge(data_frames[0], data_frames[1],  how='left', left_on=['region'], right_on = ['region'])

"""
Run the region logic to populate the region value
Use 'Edited' CSV files to remove large England summary values and unwanted columns.
See the test data for the right format, we are only using london borough, shir and met data.
"""
out = region.impute_region("data/edited/county_to_region_population_edited.csv")
out.to_csv("output/population_out.csv")
exit()
""" Sanitize """
# Get rid of anything without a region
out = out.drop(out[out.region == "0"].index)

# Some numerical values are -- so replace these
year_range = [str(i) for i in list(range(1994, 2019))]
for i in year_range:
    out[i] = out[i].replace([".."], "0")

# Group by region and preserve the variable so we can use it for reshaping
out = out.groupby(["region"], as_index=False)[year_range].sum()

# Re-shape
out = out.melt("region", var_name="Year", value_name="Housing Stock")
out = out.sort_values(by=["region", "Year"])
out = out.reset_index(drop=True)
out.to_csv("output/population_out_shaped.csv")
out.to_csv("output/population_out.csv")
