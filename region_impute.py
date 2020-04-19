import pandas as pd

from utils import region


class RegionImpute(object):
    """ Simple region imputation from one file"""

    def __init__(self, input_path, variable_name, output_path):
        self.input_path = input_path
        self.variable_name = variable_name
        self.output_path = output_path

    def impute(self):
        out = region.impute_region(self.input_path, self.variable_name)
        out.to_csv(self.output_path)


housing = RegionImpute(
    "data/edited/county_to_region_housing_stock_edited.csv",
    "Lower and Single Tier Authority Data",
    "output/final_data_files/region_data_added/housing_stock.csv",
)
# housing.impute()

population = RegionImpute(
    "data/edited/county_to_region_population_edited.csv",
    "Local Auth District",
    "output/final_data_files/region_data_added/population.csv",
)
# population.impute()


class RegionImputeMultiFile(RegionImpute):
    """Region Imputation from multiple data files """

    def __init__(self, year_range, tmp_file_path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.year_range = year_range
        self.tmp_file_path = tmp_file_path
        self.master_df = pd.DataFrame()
        # make a list of the files we are going to be using
        self.files = []
        for i in list(range(self.year_range[0], self.year_range[1])):
            i = str(i)
            self.files.append(f"{self.input_path}{i}.csv")

    def _build_data_from_files(self):
        for file in self.files:
            df = pd.read_csv(file, thousands=",")
            self.master_df = self.master_df.append(df)
        self.master_df.to_csv(self.tmp_file_path)

    def impute(self):
        self.data = self._build_data_from_files()
        out = region.impute_region(self.tmp_file_path, self.variable_name)
        out.to_csv(self.output_path)


local_council = RegionImputeMultiFile(
    input_path="data/edited/local_council_compositions_",
    variable_name="Authority",
    output_path="output/final_data_files/region_data_added/local_council.csv",
    year_range=(2015, 2016),
    tmp_file_path="output/tmp/local_council_master.csv",
)
local_council.impute()
