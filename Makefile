VENV := .venv
RUN_IN_VENV := @source ./$(VENV)/bin/activate;
all: venv

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt

venv: $(VENV)/bin/activate

lint: venv
	$(RUN_IN_VENV) isort *.py topn
	$(RUN_IN_VENV) black *.py topn
	$(RUN_IN_VENV) pylint *.py topn
	
test: venv 
	./$(VENV)/bin/python3 test.py

clean:
	$(RUN_IN_VENV) deactivate
	rm -rf $(VENV)

.PHONY: all venv test clean