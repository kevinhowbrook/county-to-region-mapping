import pandas as pd

from utils import region

"""Local coucil %
"""

# Add region and year variable

# First add a year variable to the data depending on what file we are using
# and munge all the data to one frame
file_name_range = list(range(2015, 2016))
print(file_name_range)
master_df = pd.DataFrame()
for i in file_name_range:
    i = str(i)
    file_name = f"data/edited/local_council_compositions_{i}.csv"
    df = pd.read_csv(file_name, thousands=",")
    # Iterate through the rows in the Df and for each row, fill in the region
    # as a new variable depending on the county.
    df["year"] = i
    master_df = master_df.append(df)

master_df.to_csv("output/tmp/local_council_master.csv")
# Impute the region data
out = region.impute_region("output/tmp/local_council_master.csv", "Authority", 1)
mask = out.region == "East of England"
column_name = "region"
out.loc[mask, column_name] = "South East"

out.to_csv("output/tmp/local_council_master_region_added.csv")
out.to_csv("output/final_data_files/regions/local_council.csv")

# Add year

# Reshape and group by control % and year
