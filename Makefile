install:
	python -m venv ./.venv/saynganth-one && \
	source ./.venv/saynganth-one/bin/activate && \
	pip install -r requirements.txt

remove:
	rm -rf ./.venv
