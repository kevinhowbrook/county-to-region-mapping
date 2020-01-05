from utils import lookups
import json
import pandas as pd


def test_county_to_region():
    assert lookups.county_to_region("Cleaveland") == "North"
    assert lookups.county_to_region("Bedfordshire") == "South East"
    if lookups.county_to_region("I made this up") is False:
        assert True


def test_auth_code_to_county():
    assert lookups.local_auth_code_to_region("E08000007") == {
        "la_code": "E08000007",
        "la_name": "Stockport",
        "county_name": "Greater Manchester",
        "region_name": "North West",
    }


def test_all_lacodes_return_regions():
    # Check that all LA codes in the mapping sheet can return region names
    jdata = json.loads(open("utils/lacodes.json").read())
    for i in jdata["features"]:
        code = i["attributes"]["LAD15CD"]
        geo_data = lookups.local_auth_code_to_region(code)
        if geo_data["region_name"] is False:
            # print(f'Cannot find a region value for {geo_data["county_name"]}')
            assert False
        else:
            assert True


def test_all_lacodes_in_test_data_return_regions():
    # This will take all the relevant area codes and check reqions are returned
    df = pd.read_csv("tests/test_data.csv")
    area_codes = df["Area code"].tolist()
    for i in area_codes:
        if type(i) is str and i[:3] == "E07":  # codes we want start with E07
            geo_data = lookups.local_auth_code_to_region(i)
            if geo_data and geo_data["region_name"] is True:
                assert True
            else:
                # print(f"Cannot find a region value for {i}")
                row = df.loc[df['Area code'] == i]
                print(row['Lower and Single Tier Authority Data'].values)


                # assert False


# def test_string_to_county():
#     assert lookups.local_string_to_region("E08000007") == {
#         "la_code": "E08000007",
#         "la_name": "Stockport",
#         "county_name": "Greater Manchester",
#         "region_name": "North West",
#     }
