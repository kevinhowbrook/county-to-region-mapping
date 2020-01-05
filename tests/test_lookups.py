from utils import lookups
import json
import pandas as pd


def test_county_to_region():
    assert lookups.county_to_region("Cleaveland") == "North"
    assert lookups.county_to_region("Bedfordshire") == "South East"
    if lookups.county_to_region("I made this up") is False:
        assert True


# TODO
# def test_all_strings_in_test_housing_data_return_regions():
#     df = pd.read_csv("tests/test_housing_data.csv")
#     places = df["Lower and Single Tier Authority Data"].tolist()
#     not_mapped = []
#     for i in places:
#         geo_data = lookups.local_string_to_region(i)
#         if geo_data and geo_data["region_name"] != "":
#             pass
#         else:
#             # print(f"Cannot find a region value for {i}")
#             not_mapped.append(i)
#             # row = df.loc[df["Lower and Single Tier Authority Data"] == i]
#             # print(row["Lower and Single Tier Authority Data"].values)
#             assert False
#     #print(list(set(not_mapped)))


def test_all_strings_in_test_population_age_data_return_regions():
    df = pd.read_csv("tests/test_population_data.csv")
    places = df["Local Auth District"].tolist()
    places = list(set(places))
    not_mapped = []
    for i in places:
        geo_data = lookups.local_string_to_region(i)
        if geo_data and geo_data["region_name"] != "":
            print(geo_data)
            pass
        else:
            # print(f"Cannot find a region value for {i}")
            not_mapped.append(i)
            # row = df.loc[df["Lower and Single Tier Authority Data"] == i]
            # print(row["Lower and Single Tier Authority Data"].values)
            assert False
            # print(list(set(not_mapped)))


# Can all la_strings in the test data return a county?
# TODO once we have assumed missing place counties
def test_all_strings_in_mapping_data_can_return_regions():
    jdata = json.loads(open("utils/lacodes.json").read())
    for i in jdata:
        if i["CTRY17NM"] == "England":
            county_name = i["CTY17NM"]
            if county_name:
                region_name = lookups.county_to_region(county_name)
            else:
                region_name = i["GOR10NM"]
            assert region_name


def test_string_to_county_to_region():
    assert lookups.local_string_to_region("Chichester") == {
        "la_code": "E07000225",
        "la_name": "Chichester",
        "county_name": "West Sussex",
        "region_name": "South East",
    }


def test_string_no_county_return_region():
    assert lookups.local_string_to_region("Bedford") == {
        "la_code": "E06000055",
        "la_name": "Bedford",
        "county_name": "",
        "region_name": "East of England",
    }
