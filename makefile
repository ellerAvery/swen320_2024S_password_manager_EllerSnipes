.PHONY: install run

install:
	pip install -r requirements.txt

run:
	dotenv run python3 manage.py run -p 8080
