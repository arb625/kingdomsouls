test:
	pipenv run pytest

coverage:
	pipenv run pytest --cov=kingdomsouls

mypy:
	pipenv run mypy kingdomsouls

lint:
	pipenv run flake8
