import json

geography = {
    "North": [
        "Cleaveland",
        "Durham",
        "Northumberland",
        "Tyne & Wear",
        "Tyne and Wear",
        "Tyne and Wear (Met County)",
    ],
    "North West": [
        "Cumbria",
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
        "Cornwall and the Isles of Scilly",
        "Devon",
        "Dorset",
        "Gloucestershire",
        "Somerset",
        "Wiltshire",
    ],
    "East Anglia": ["Cambridgeshire", "Norfolk", "Suffolk"],
    "South East": [
        "Bedford",
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

# Shouldnt have south east or east of england
# these should

# East of england should be South East

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


# def local_auth_code_to_region(code):
#     """LAcode to region
#     Arguments:
#         code: string -- the LA Code, eg E08000007
#     Returns:
#         dict -- la_code, la_name, county_name, region_name
#     """
#     county = False
#     for i in jdata:
#         if str(code) in i["LAD19CD"]:
#             county_name = i["attributes"]["CTY15NM"]
#             la_name = (
#                 i["attributes"]["LAD15NM"] if i["attributes"]["LAD15NM"] else False
#             )
#             region_name = county_to_region(county_name)

#             return {
#                 "la_code": code,
#                 "la_name": la_name,
#                 "county_name": county_name,
#                 "region_name": region_name,
#             }


def local_string_to_region(la_string, map_counties=0):

    if la_string[-3:] == " UA":
        la_string = la_string[:-2]
    """LAcode to region
    Arguments:
        la_string: string -- the LA name eg, Bedford
        map_counties: int -- if 1, then after failing to map the LA on LAD17NM
            attempt to map it as a county: CTY17NM
    Returns:
        dict -- la_code, la_name, county_name, region_name
    """
    for i in jdata:
        # if la is peterborough return something foced
        if la_string == "Peterborough":
            return {
                "la_code": i["LAD17CD"],
                "la_name": la_string,
                "county_name": "Cambridgeshire",
                "region_name": "East Anglia",
            }
        if la_string == i["LAD17NM"]:
            # If there is no county assigned, we can't look it up in our mapping
            # So use the region name in the data, it's about 52 places that do this
            county_name = i["CTY17NM"]
            if county_name:
                region_name = county_to_region(county_name)
            else:
                region_name = i["GOR10NM"]
            if (
                region_name == "Yorkshire & Humberside"
                or region_name == "Yorkshire and The Humber"
            ):
                region_name = "Yorkshire & Humberside"
            return {
                "la_code": i["LAD17CD"],
                "la_name": la_string,
                "county_name": county_name,
                "region_name": region_name,
            }
        if la_string == i["CTY17NM"] and map_counties == 1:
            print("here")
            region_name = county_to_region(la_string)
            if (
                region_name == "Yorkshire & Humberside"
                or region_name == "Yorkshire and The Humber"
            ):
                region_name = "Yorkshire & Humberside"
            return {
                "la_code": i["LAD17CD"],
                "la_name": la_string,
                "county_name": i["CTY17NM"],
                "region_name": region_name,
            }
