import glob
import pandas as pd
from utils import region
import numpy as np


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
"""
# TODO
The data needs variable with ages in ranges E.G, female 16 > 19
This is really f'ing confusing to read
"""

df = pd.read_csv('tests/test_population_data.csv')
# Not interested in anything below 16
df = df.drop(df[df.age < 16].index)
df = df.head(1000)
places = list(set(df["Local Auth District"].tolist()))
places.sort()
age_ranges = list(chunks(list(range(15, 91)), 5))
year_ranges = [str(i) for i in list(range(2001, 2018))]
range_data = pd.DataFrame()

# Loops through each place (area code/LA)
for place in places:
    print(place)
    """Make a dictionary for adding the data to, then add it to the rande_data dataframe
    E,G:
    {'Male 15 > 19': '', 'Male 20 > 24': '', 'Male 25 > 29': '', 'Male 30 > 34': '', 'Male 35 > 39': '', 'Male 40 > 44': '', 'Male 45 > 49': '', 'Male 50 > 54': '', 'Male 55 > 59': '', 'Male 60 > 64': '', 'Male 65 > 69': '', 'Male 70 > 74': '', 'Male 75 > 79': '', 'Male 80 > 84': '', 'Male 85 > 89': '', 'Male 90 > 90': '', 'Female 15 > 19': '', 'Female 20 > 24': '', 'Female 25 > 29': '', 'Female 30 > 34': '', 'Female 35 > 39': '', 'Female 40 > 44': '', 'Female 45 > 49': '', 'Female 50 > 54': '', 'Female 55 > 59': '', 'Female 60 > 64': '', 'Female 65 > 69': '', 'Female 70 > 74': '', 'Female 75 > 79': '', 'Female 80 > 84': '', 'Female 85 > 89': '', 'Female 90 > 90': '', 'Local Auth Disctrict': 'Warrington', 'Year': '2017'}
    """
    for i in year_ranges:
        a_row = {}
        for a in age_ranges:
            a_row.update({
                f"Male {a[0]} > {a[-1]}": ''
            })
        for a in age_ranges:
            a_row.update({
                f"Female {a[0]} > {a[-1]}": ''
            })
        a_row.update({
            "Local_Auth_Disctrict": place,
            "Year": i
        })
        range_data = range_data.append(a_row, ignore_index=True)


    # Populating the age data:
    temp_data = df.loc[df['Local Auth District'] == place]
    # Now we have a temp data frame of 1 area.
    # Sum year data and by year ranges, male then female
    # 1 = male, 2 = female
    for age in age_ranges:
        dt = temp_data.loc[
            (temp_data["age"].isin(age))
            & (temp_data["sex"] == 1)
        ]
        var_name = f"Male {age[0]} > {age[-1]}"  # e,g male 15 > 19
        for i in year_ranges:
            # now dt is a dataframe of eg 16 > 19., Darlington, male
            # Sum up the population_year values and add them to range_data
            vals = sum(list(set(dt[f"population_{i}"].tolist())))
            # Vals is now equal to age range at year at place, so add it :/
            # find in the ranged data frame where this needs to be added
            range_data.loc[
                (range_data.Year == i) &
                (range_data.Local_Auth_Disctrict == place),
                var_name] = vals
    # dupe for ladies
    for age in age_ranges:
        dt = temp_data.loc[
            (temp_data["age"].isin(age))
            & (temp_data["sex"] == 2)
        ]
        var_name = f"Female {age[0]} > {age[-1]}"  # e,g male 15 > 19
        for i in year_ranges:
            # now dt is a dataframe of eg 16 > 19., Darlington, male
            # Sum up the population_year values and add them to range_data
            vals = sum(list(set(dt[f"population_{i}"].tolist())))
            # Vals is now equal to age range at year at place, so add it :/
            # find in the ranged data frame where this needs to be added
            range_data.loc[
                (range_data.Year == i) &
                (range_data.Local_Auth_Disctrict == place),
                var_name] = vals


range_data.to_csv("output/population_out_ranges_added.csv")
exit()
"""
Run the region logic to populate the region value
Use 'Edited' CSV files to remove large England summary values and unwanted columns.
See the test data for the right format, we are only using london borough, shir and met data.
"""
# out = region.impute_region("data/edited/county_to_region_population_edited.csv", "Local Auth District")
out = region.impute_region(
    "tests/test_population_data_small.csv", "Local Auth District"
)
out.to_csv("output/population_out.csv")
""" Sanitize """
# Get rid of anything without a region
out = out.drop(out[out.region == "0"].index)

# Some numerical values are -- so replace these
year_range = [f"population_{str(i)}" for i in list(range(2001, 2017))]

for i in year_range:
    out[i] = out[i].replace([".."], "0")

# Group by region and preserve the variable so we can use it for reshaping
out = out.groupby(["region", "sex"], as_index=False)[year_range].sum()
out.to_csv("output/population_out_grouped.csv")

# Re-shape
# out = out.melt("region", var_name="Year", value_name="Housing Stock")
# out = out.sort_values(by=["region", "Year"])
# out = out.reset_index(drop=True)
# out = (
#     out.melt(id_vars=["region", "sex"], var_name="Year")
#     .set_index(["sex", "region", "Year"])
#     .squeeze()
#     .unstack()
#     .reset_index()
# )
# out = out.sort_values(by=["region"])
out.to_csv("output/population_out_shaped.csv")
out.to_csv("output/population_out.csv")
