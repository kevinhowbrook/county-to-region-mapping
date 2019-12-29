import pandas as pd

from utils import region


def test_region_returns_df():
    df = region.impute_region("data/county_to_region_housing_stock.xlsx-LT116.csv")
    assert type(df) == pd.core.frame.DataFrame


def test_region_is_added_df():
    df = region.impute_region("data/county_to_region_housing_stock.xlsx-LT116.csv")
    regions = list(set(df["region"].values.tolist()))
    # Remove the empty strings
    regions = list(filter(None, regions))
    assert len(regions) > 0
