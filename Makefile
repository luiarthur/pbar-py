VENV = venv-tmp
ACT = . $(VENV)/bin/activate

init:
	python3 -m venv $(VENV) && \
		$(ACT)  && \
		pip install -U pip && \
		pip install .

test:
	$(ACT) && \
		pip install . && \
		python -m unittest --verbose
