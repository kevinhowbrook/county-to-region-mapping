[![Maintainability](https://api.codeclimate.com/v1/badges/368dc1652646431ef8ff/maintainability)](https://codeclimate.com/github/kevinhowbrook/county-to-region-mapping/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/368dc1652646431ef8ff/test_coverage)](https://codeclimate.com/github/kevinhowbrook/county-to-region-mapping/test_coverage) [![CircleCI](https://circleci.com/gh/kevinhowbrook/county-to-region-mapping.svg?style=svg)](https://circleci.com/gh/kevinhowbrook/county-to-region-mapping)

## Run locally

This project uses poetry, so run:
```poetry install```
or
``` poetry run foo```

## Tests

Run tests with `pytest`, or `poetry run pytest`

or better without cache...

```poetry run pytest -p no:cacheprovider```

## Notes

Following county > regions were assumptions
 - West Midlands (Met County)
 - Worcestershire
 - Greater Manchester (Met County)
 - South Yorkshire (Met County)
 - Lancashire
 - Northamptonshire
 - Tyne and Wear (Met County)
 - Merseyside (Met County)
 - West Yorkshire (Met County)
 - Met and Shire Counties
 - Cornwall and Isles of Scilly

## TODOs
#### Create lookup function from area code to region
Use this for mapping https://services1.arcgis.com/ESMARspQHYMw9BZ9/arcgis/rest/services/LAD15_CTY15_EN_LU/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json.
We need to be able to query a LA code, eg E1100001 and return a region.
This will be LACODE > country > region.
For the county lookup we may need to use utils.mapping


#### Others
- Create method in utils for creating new variable for ssr from county
- Merge data set on year and region variable and sum values
- tests should use a mock csv
