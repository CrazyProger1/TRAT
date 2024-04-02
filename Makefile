.PHONY: build
build:
	poetry run pyinstaller -F --name TRAT main.py

.PHONY: run
run:
