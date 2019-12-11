
main: venv/lib/python3.*/site-packages/git
	venv/bin/python main.py

venv/lib/python3.7*/site-packages/git: venv/bin/pip
	venv/bin/pip install -r requirements.txt

venv/bin/pip:
	python3 -m venv venv


