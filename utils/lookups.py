import json


geography = {
    "North": [
        "Cleaveland",
        "Durham",
        "Northumberland",
        "Tyne & Wear",
        "Tyne and Wear",
        "Cumbria",
        "Tyne and Wear (Met County)",
    ],
    "North West": [
        "Cheshire",
        "Greater Manchester",
        "Lancashire",
        "Merseyside",
        "Merseyside (Met County)",
        "Greater Manchester",
        "Greater Manchester (Met County)",
    ],
    "Yorkshire & Humberside": [
        "Humberside",
        "North Yorkshire",
        "South Yorkshire",
        "South Yorkshire (Met County)",
        "West Yorkshire",
        "West Yorkshire (Met County)",
    ],
    "East Midlands": [
        "Derbyshire",
        "Leicestershire",
        "Lincolnshire",
        "Northamptonshire",
        "Nottinghamshire",
    ],
    "West Midlands": [
        "Hereford & Worcester",
        "Worcestershire",
        "Shropshire",
        "Staffordshire",
        "Warwickshire",
        "West Midlands",
        "West Midlands (Met County)",
    ],
    "South West": [
        "Avon",
        "Cornwall",
        "Cornwall and Isles of Scilly",
        "Devon",
        "Dorset",
        "Gloucestershire",
        "Somerset",
        "Wiltshire",
    ],
    "East Anglia": ["Cambridgeshire", "Norfolk", "Suffolk"],
    "South East": [
        "Bedfordshire",
        "Essex",
        "Hertfordshire",
        "Greater London",
        "Berkshire",
        "Buckinghamshire",
        "East Sussex",
        "Hampshire",
        "Isle of Wight",
        "Kent",
        "Oxfordshire",
        "Surrey",
        "West Sussex",
        "Inner London",
        "Outer London",
    ],
    "Unknown": ["Met and Shire Counties"],
}


"""
Given a county input, return it's SSR (Standard Statistical Region)
"""


def county_to_region(county):
    region = False
    for r, c in geography.items():
        if county in c:
            region = r
    return region


jdata = json.loads(open("utils/lacodes.json").read())


def local_auth_code_to_region(code):
    """LAcode to region
    Arguments:
        code: string -- the LA Code, eg E08000007
    Returns:
        dict -- la_code, la_name, county_name, region_name
    """
    county = False
    for i in jdata["features"]:
        if str(code) in i["attributes"]["LAD15CD"]:
            county_name = i["attributes"]["CTY15NM"]
            la_name = (
                i["attributes"]["LAD15NM"] if i["attributes"]["LAD15NM"] else False
            )
            region_name = county_to_region(county_name)

            return {
                "la_code": code,
                "la_name": la_name,
                "county_name": county_name,
                "region_name": region_name,
            }


def local_string_to_region(code):
    """LAcode to region
    Arguments:
        code: string -- the LA Code, eg E08000007
    Returns:
        dict -- la_code, la_name, county_name, region_name
    """
    county = False
    for i in jdata["features"]:
        if str(code) in i["attributes"]["LAD15CD"]:
            county_name = i["attributes"]["CTY15NM"]
            la_name = (
                i["attributes"]["LAD15NM"] if i["attributes"]["LAD15NM"] else False
            )
            region_name = county_to_region(county_name)

            return {
                "la_code": code,
                "la_name": la_name,
                "county_name": county_name,
                "region_name": region_name,
            }
