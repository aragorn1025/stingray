up:
	poetry run uvicorn stingray.main:app --host 0.0.0.0 --port 8000 --reload
.PHONY: up

install:
	poetry install
.PHONY: install

lint:
	poetry run isort .
	poetry run black .
	poetry run flake8
.PHONY: lint

clean:
	rm -rf .venv/
.PHONY: clean
