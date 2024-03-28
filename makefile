.PHONY: install run test setup coverage coverage_html check_docker

DOCKER_IMAGE_NAME := flask_app
FLASK_PORT := 8080

check_docker:
	@echo "Checking Docker status and image..."
	@python check_docker.py

install: check_docker
	@echo "Installing Python dependencies..."
	@pip install -r requirements.txt
	# No need to build the Docker image here if it already exists - handled by check_docker.py

setup: install

run:
	@echo "Starting Flask application..."
	@docker run -d -p $(FLASK_PORT):5000 $(DOCKER_IMAGE_NAME)

test:
	@echo "Running tests..."
	@python manage.py test

coverage:
	@echo "Generating coverage reports..."
	@coverage run -m unittest discover -v web/test
	@coverage report -m
	@coverage html
	@echo "Reports generated. Check the console and htmlcov/index.html."
