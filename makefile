.PHONY: install run test setup check-docker

# Set up variables for Docker image name and Flask app port
DOCKER_IMAGE_NAME := flask_app
CONTAINER_NAME := flask_app_container
FLASK_PORT := 8080

# Installation tasks for Python dependencies and Docker setup
install:
	@echo "Installing Python dependencies from requirements.txt..."
	pip install -r requirements.txt

# Check Docker status, run Docker if needed, and perform installation if Docker isn't set up
setup:
	@echo "Checking Docker status and setting up environment..."
	@python check_docker.py || (echo "Setting up Docker environment..." && make install && docker build -t $(DOCKER_IMAGE_NAME) . && python check_docker.py)

# Run application without Docker
run:
	@echo "Starting Flask application on port $(FLASK_PORT)..."
	@python -m dotenv run python manage.py run -p $(FLASK_PORT)

# Running tests
test:
	@python manage.py test

# Generating coverage report
coverage:
	@echo "Generating coverage report..."
	@coverage run -m unittest discover -v web/test
	@coverage report -m
	@coverage html
	@echo "HTML coverage report generated."

