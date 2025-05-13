run:
	python mejorcdt/main.py

test:
	pytest

install:
	pip install -r requirements.txt

format:
	black mejorcdt/ tests/
