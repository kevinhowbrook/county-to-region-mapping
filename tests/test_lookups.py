from utils import lookups
import json


def test_county_to_region():
    assert lookups.county_to_region("Cleaveland") == "North"
    assert lookups.county_to_region("Bedfordshire") == "South East"
    if lookups.county_to_region("I made this up") is False:
        assert True


def test_auth_code_to_county():
    assert lookups.local_auth_code_to_county("E08000007") == {
        "la_code": "E08000007",
        "la_name": "Stockport",
        "county_name": "Greater Manchester",
        "region_name": "North West",
    }


def test_all_lacodes_return_regions():
    # Check that all LA codes we have in the json return region names
    jdata = json.loads(open("utils/lacodes.json").read())
    for i in jdata["features"]:
        code = i["attributes"]["LAD15CD"]
        geo_data = lookups.local_auth_code_to_county(code)
        if geo_data["region_name"] is False:
            # print(f'Cannot find a region value for {geo_data["county_name"]}')
            assert False
        else:
            assert True
