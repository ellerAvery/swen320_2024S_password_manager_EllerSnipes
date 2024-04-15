.PHONY: install run test setup coverage coverage_html

install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt
	docker build -t flask .
		
setup: install

run:
	@echo "Starting application..."
	python -m dotenv run python manage.py run -p 8080

test:
	@echo "Running tests..."
	python manage.py test # Adjust if you have a specific Flask command for tests

coverage:
	@echo "Generating coverage report..."
	coverage run -m unittest discover -v web/test # Specify your test directory if not the default
	coverage report -m

coveragehtml:
	@echo "Generating HTML coverage report..."
	coverage run -m unittest discover -v web/test 
	coverage html
	@echo "Open htmlcov/index.html in your browser to view the report."