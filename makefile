.PHONY: install run test setup coverage coverage_html

# Set up variables for docker container name and port options for running the Flask app
DOCKER_IMAGE_NAME := flask_app
FLASK_PORT := 8080

# Installation tasks
install:
	@echo "Installing Python dependencies from requirements.txt..."
	@pip install -r requirements.txt
	@echo "Building Docker image $(DOCKER_IMAGE_NAME)..."
	@docker build -t $(DOCKER_IMAGE_NAME) .

setup: install

# Running the application
run:
	@echo "Starting Flask application on port $(FLASK_PORT)..."
	@python -m dotenv run python manage.py run -p $(FLASK_PORT)

# Running tests
test:
	@echo "Running unit tests..."
	@python manage.py test

# Generating coverage report in command-line
coverage:
	@echo "Generating coverage report..."
	@coverage run -m unittest discover -v web/test
	@coverage report -m
	@coverage run -m unittest discover -v web/test
	@coverage html
	@echo "HTML coverage report generated. Open htmlcov/index.html in your browser to view the report."
