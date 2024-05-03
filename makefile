.PHONY: install run test setup coverage coverage_html

install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt
	docker build -t flask .

setup: install

run:
	@echo "Starting application..."
	python -m dotenv run -- python manage.py run -p 8080

test:
	@echo "Running tests..."
	python -m dotenv run -- python manage.py test

coverage:
	@echo "Generating coverage report..."
	coverage run manage.py test # Specify your test directory if not the default
	coverage report -m

coverage_html:
	@echo "Generating HTML coverage report..."
	coverage run manage.py test
	coverage html
	@echo "Open htmlcov/index.html in your browser to view the report."

coverage_branch:
	@echo "Generating HTML coverage report..."
	coverage run --branch manage.py test
	coverage html
	@echo "Open htmlcov/index.html in your browser to view the report."