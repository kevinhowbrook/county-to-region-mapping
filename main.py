import glob

from utils import region

""" Loop over all the data files and populate region data """
for f in glob.glob("data/*.csv"):
    df = region.impute_region(f)
    print(df)

""" Merge all the new data to one data set on Year and Region """
