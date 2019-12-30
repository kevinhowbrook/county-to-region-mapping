import glob
import pandas as pd
from utils import region


""" Loop over all the data files and populate region data
and make a list of dataframes to merge """
data_frames = []

for i,f in enumerate(glob.glob("data/*.csv")):
    data_frames.append(region.impute_region(f))

new_df = []
for d in data_frames:
    for i, row in enumerate(d.itertuples()):  # enumeration means the row begins 0
        new_df.append(row)

out = pd.DataFrame(new_df)
""" Merge all the new data to one data set on Year and Region """
#new_df = pd.merge(data_frames[0], data_frames[1],  how='left', left_on=['region'], right_on = ['region'])
out.to_csv('output/out.csv')