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

No idea what Met and Shire Counties is

## TODOs
- Make data frame similar to one in the data
 - Check spelling of county names in dataframe match utils.mapping
- Create method in utils for creating new variable for ssr from county
- Create test for new method to ammend/create new data variable.
- Merge data set on year and region variable

