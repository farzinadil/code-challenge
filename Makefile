# Makefile

# Python interpreter to use
PYTHON = python3

# Path to the main script
MAIN_SCRIPT = src/scrape.py

# Directory containing tests
TEST_DIR = tests

# Virtual environment directory
VENV = venv

# Virtual environment activation
VENV_ACTIVATE = $(VENV)/bin/activate

# Install dependencies and set up virtual environment
.PHONY: install
install:
	$(PYTHON) -m venv $(VENV)
	. $(VENV_ACTIVATE) && pip install -r requirements.txt


# Run the main script
.PHONY: run
run:
	. $(VENV_ACTIVATE) && $(PYTHON) $(MAIN_SCRIPT)

# Run all tests
.PHONY: test
test:
	. $(VENV_ACTIVATE) && $(PYTHON) -m unittest discover $(TEST_DIR)

.PHONY: clean
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf $(VENV)
	rm -f files/generated_array.json

# Help command to show available commands
.PHONY: help
help:
	@echo "Available commands:"
	@echo "  make install          Install dependencies and set up virtual environment"
	@echo "  make run              Run the main script"
	@echo "  make test             Run all tests"
	@echo "  make clean            Clean up pyc files, virtual environment, and generated_array.json"