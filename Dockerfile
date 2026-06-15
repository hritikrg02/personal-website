FROM python:3.13-alpine

COPY requirements.txt .
COPY .venv .

RUN python -m venv ./.venv/saynganth-one && \
	source ./.venv/saynganth-one/bin/activate && \
	pip install -r requirements.txt


CMD ["python", "main.py"]
