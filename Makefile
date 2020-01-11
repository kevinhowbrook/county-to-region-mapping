test-local:
	poetry run pytest -p no:cacheprovider

run:
	poetry run python main.py

run-all:
	poetry run python housing_stock.py
	poetry run python population.py
