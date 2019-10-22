test:
	pipenv run python -m pytest

coverage:
	pipenv run python -m pytest --cov=kingdomsouls

coverage-html:
	pipenv run python -m pytest --cov=kingdomsouls --cov-report=html

type-check:
	pipenv run mypy kingdomsouls

lint:
	pipenv run flake8
