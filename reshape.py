import glob
import pandas as pd
from utils import region

out = pd.read_csv('output/out.csv')
#out = region.impute_region('tests/test_data.csv')
""" Sanitize """
#out = out.melt('region', var_name="Year", value_name="Year")
out = out.melt("region", var_name="Year", value_name="Housing Stock")
out = out.sort_values(by=['region', 'Year'])
out = out.reset_index(drop=True)
out.to_csv("output/out_shaped.csv")


