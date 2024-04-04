.PHONY: build
build:
	poetry run pyinstaller -w -F --name TRAT -i resources/images/logo.ico trat/__main__.py --add-data ".env:."

.PHONY: build-debug
build-debug:
	poetry run pyinstaller -F --name TRAT-Debug trat/__main__.py --add-data ".env:."

.PHONY: run
run:
	poetry run python -m trat

.PHONY: install
install:
	poetry install

.PHONY: format
format:
	poetry run python -m black trat/__main__.py

.PHONY: test
test:
	poetry run python -m pytest tests