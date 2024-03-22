.PHONY: install run test setup coverage coverage_html

install:
	pip install -r requirements.txt

setup:
	pip install -r requirements.txt

run:
	python -m dotenv run python manage.py run -p 8080

test:
	python manage.py test

coverage:
	coverage run -m unittest discover -v
	coverage report -m

coverage_html:
	coverage run -m unittest discover -v
	coverage html
	@echo "HTML coverage report generated in the 'htmlcov/' directory"