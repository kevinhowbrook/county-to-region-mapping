test-local:
	poetry run pytest -p no:cacheprovider

run:
	poetry run python main.py