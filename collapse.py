import glob
import pandas as pd
from utils import region


""" Loop over all the data files and populate region data
and make a list of dataframes to merge """
data_frames = []

out = region.impute_region('data/county_to_region_housing_stock_edited.csv')
#out = region.impute_region('tests/collapse_test_data.csv')
""" Sanitize """
# Get rid of anything without a region
out = out.drop(out[out.region == '0'].index)

# Some numerical values are -- so replace these
year_range = [str(i) for i in list(range(1994,2019))]
for i in year_range:
    out[i] = out[i].replace(['..'], '0')


out.to_csv("output/small_test_data_region_added.csv")

#out = out.set_index('region').groupby(['region'])[year_range].sum()
out = out.groupby(['region'], as_index=False)[[str(i) for i in list(range(1994,2019))]].sum()


out.to_csv("output/test_collapse_out.csv")
