from utils import mapping


def test_mapping():
    assert mapping.county_to_region("Cleaveland") == "North"
    assert mapping.county_to_region("Bedfordshire") == "South East"
    if mapping.county_to_region("I made this up") is False:
        assert True
