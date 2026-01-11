# system python interpreter. used only to create virtual environment
PY=python3
VENV?=.venv
BIN=$(VENV)/bin

$(VENV): requirements.txt requirements-dev.txt
	$(PY) -m venv $(VENV)
	$(BIN)/pip install --upgrade -r requirements.txt
	$(BIN)/pip install --upgrade -r requirements-dev.txt
	touch $(VENV)

.phony: init
init: $(VENV)

.PHONY: test
test: $(VENV)
	$(BIN)/pytest

.PHONY: dev
dev: $(VENV) src/server.py
	$(BIN)/python src/server.py

clean:
	rm -rf $(VENV)
	find . -type f -name *.pyc -delete
	find . -type d -name __pycache__ -delete
