run: venv
	.venv/bin/python -m main

test: venv
	.venv/bin/pytest -vv test.py

repl: venv
	.venv/bin/python

venv: .venv/bin/activate

.venv/bin/activate: requirements.txt
	test -d .venv || python3 -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -U pytest
	.venv/bin/pip install -r requirements.txt
	touch .venv/bin/activate
