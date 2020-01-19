import pandas as pd

from utils import region


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def populate_age_data(gender, sex, ages, temp_data, range_data, year_ranges, place):
    for age in ages:
        dt = temp_data.loc[(temp_data["age"].isin(age)) & (temp_data["sex"] == sex)]
        var_name = f"{gender} {age[0]} > {age[-1]}"  # e,g male 15 > 19
        for i in year_ranges:
            # now dt is a dataframe of eg 16 > 19., Darlington, male
            # Sum up the population_year values and add them to range_data
            vals = sum(list(set(dt[f"population_{i}"].tolist())))
            # Vals is now equal to age range at year at place, so add it
            # find in the ranged data frame where this needs to be added
            range_data.loc[
                (range_data.Year == i) & (range_data.Local_Auth_District == place),
                var_name,
            ] = vals


"""
Part 1
The data needs variable with ages in ranges E.G, female 16 > 19
This is really f'ing confusing to read
"""


def part_one():
    df = pd.read_csv("data/edited/county_to_region_population_edited.csv")
    # Not interested in anything below 16
    df = df.drop(df[df.age < 16].index)
    places = list(set(df["Local Auth District"].tolist()))
    places.sort()
    age_ranges = list(chunks(list(range(15, 65)), 5))
    age_ranges.append(list(range(65, 91)))
    year_ranges = [str(i) for i in list(range(2001, 2018))]
    range_data = pd.DataFrame()

    # Loops through each place (area code/LA)
    for place in places:
        """Make a dictionary for adding the data to, then add it to the rande_data dataframe
        E,G:
        {'Male 15 > 19': '', 'Male 20 > 24': '', 'Male 25 > 29': '', 'Male 30 > 34': '', 'Male 35 > 39': '', 'Male 40 >
        44': '', 'Male 45 > 49': '', 'Male 50 > 54': '', 'Male 55 > 59': '', 'Male 60 > 64': '', 'Male 65 > 69': '',
        'Male 70 > 74': '', 'Male 75 > 79': '', 'Male 80 > 84': '', 'Male 85 > 89': '', 'Male 90 > 90': '', 'Female 15 >
         19': '', 'Female 20 > 24': '', 'Female 25 > 29': '', 'Female 30 > 34': '', 'Female 35 > 39': '', 'Female 40 >
         44': '', 'Female 45 > 49': '', 'Female 50 > 54': '', 'Female 55 > 59': '', 'Female 60 > 64': '', 'Female 65 >
         69': '', 'Female 70 > 74': '', 'Female 75 > 79': '', 'Female 80 > 84': '', 'Female 85 > 89': '', 'Female 90 >
         90': '', 'Local Auth Disctrict': 'Warrington', 'Year': '2017'}
        """
        for i in year_ranges:
            a_row = {}
            for a in age_ranges:
                a_row.update({f"Male {a[0]} > {a[-1]}": ""})
            for a in age_ranges:
                a_row.update({f"Female {a[0]} > {a[-1]}": ""})
            a_row.update({"Local_Auth_District": place, "Year": i})
            range_data = range_data.append(a_row, ignore_index=True)

        # Populating the age data:
        temp_data = df.loc[df["Local Auth District"] == place]
        # Now we have a temp data frame of 1 area.
        # Sum year data and by year ranges, male then female
        # 1 = male, 2 = female
        populate_age_data(
            "Male", 1, age_ranges, temp_data, range_data, year_ranges, place
        )
        populate_age_data(
            "Female", 2, age_ranges, temp_data, range_data, year_ranges, place
        )

    range_data.to_csv("output/population_out_ranges_added.csv")


part_one()

"""
Part 2
Run the region logic to populate the region value
Use 'Edited' CSV files to remove large England summary values and unwanted columns.
See the test data for the right format, we are only using london borough, shir and met data.
"""
out = region.impute_region(
    "output/population_out_ranges_added.csv", "Local_Auth_District"
)
out.to_csv("output/population_out.csv")
""" Sanitize """
# Get rid of anything without a region
out = out.drop(out[out.region == "0"].index)

mask = out.region == "East of England"
column_name = "region"
out.loc[mask, column_name] = "South East"

# Some numerical values are -- so replace these
age_ranges = list(chunks(list(range(15, 65)), 5))
age_ranges.append(list(range(65, 91)))
year_range = []
for i in age_ranges:
    year_range.append(f"Male {i[0]} > {i[-1]}")
for i in age_ranges:
    year_range.append(f"Female {i[0]} > {i[-1]}")
for i in year_range:
    out[i] = out[i].replace([".."], "0")

# Group by region and year
out = out.groupby(["region", "Year"], as_index=False)[year_range].sum()
out.to_csv("output/population_out_grouped.csv")
out.to_csv("output/final_data_files/population.csv")
