import glob
import pandas as pd
from utils import region


""" Loop over all the data files and populate region data
and make a list of dataframes to merge """
data_frames = []

#out = region.impute_region('data/county_to_region_housing_stock.xlsx-LT116.csv')
out = region.impute_region('tests/small_test_data.csv')
out = out.drop(out[out.region == '0'].index)
out.to_csv("output/small_test_data_region_added.csv")
df = out


mapping = {'1994': '1994',
           '1995': '1995',
           '1996': '1996',
           '1997': '1997'}

year_range = [str(i) for i in list(range(1994,2019))]

#df = out.set_index('region').groupby(['region'])[year_range].sum()

df = df.groupby(['region'], as_index=False)[year_range].sum()


df.to_csv("output/test_collapse_out.csv")
