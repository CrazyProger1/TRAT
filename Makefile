.PHONY: build
build:
	poetry run pyinstaller -F --name TRAT trat/__main__.py --add-data ".env:."

.PHONY: run
run:
	poetry run python -m trat


.PHONY: install
install:
	poetry install


.PHONY: format
format:
	poetry run python -m black trat/__main__.py
