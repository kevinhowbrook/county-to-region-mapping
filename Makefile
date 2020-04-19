test-local:
	poetry run pytest -p no:cacheprovider

run:
	poetry run python main.py

run-all:
	poetry run python region_impute.py

