.PHONY: install run test setup

install:
	pip install -r requirements.txt

setup:
	pip install -r requirements.txt && \
	source .env

run:
	python -m dotenv run python manage.py run -p 8080

test:
	python manage.py test

coverage:
	coverage run -m unittest discover -v && \
	coverage report -m