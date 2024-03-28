.PHONY: install run test setup coverage coverage_html check_docker

# Variables for Docker image name and Flask port
DOCKER_IMAGE_NAME := flask_app
FLASK_PORT := 8080

# Check if Docker is running using the Python script
check_docker:
	@echo "Checking if Docker is running..."
	@python check_docker.py

# Installation tasks including Docker check
install: check_docker
	@echo "Installing Python dependencies from requirements.txt..."
	@pip install -r requirements.txt
	@echo "Building Docker image $(DOCKER_IMAGE_NAME) if it doesn't exist..."
	@python check_docker_image.py $(DOCKER_IMAGE_NAME)

setup: install

# Run the application
run:
	@echo "Starting Flask application on port $(FLASK_PORT)..."
	@flask run -p $(FLASK_PORT)

# Run tests
test:
	@echo "Running unit tests..."
	@flask custom test

# Generate coverage report in command-line and HTML
coverage:
	@echo "Generating coverage report..."
	@coverage run -m unittest discover -v web/test
	@coverage report -m
	@echo "Generating HTML coverage report..."
	@coverage html
	@echo "HTML coverage report generated. Open htmlcov/index.html in your browser to view the report."
