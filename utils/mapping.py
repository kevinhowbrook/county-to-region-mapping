"""Mapping
Given a county input, return it's SSR (Standard Statistical Region)
"""


geography = {
    "North": [
        "Cleaveland",
        "Durham",
        "Northumberland",
        "Tyne & Wear",
        "Cumbria",
        "Tyne and Wear (Met County)",
    ],
    "North West": [
        "Cheshire",
        "Greater Manchester",
        "Lancashire",
        "Mersyside",
        "Merseyside (Met County)",
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
    ],
    "Unknown": ["Met and Shire Counties"],
}


def county_to_region(county):
    region = False
    for r, c in geography.items():
        if county in c:
            region = r
    return region
