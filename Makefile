create_env:
	python -m venv ./.venv/saynganth-one && \
	. ./.virtualenvs/saynganth-one/bin/activate && \
	pip install -r requirements.txt

remove_env:
	rm -rf ./.venv/saynganth-one

dev:
	docker compose -f docker-compose.dev.yml up --build -d

prod:
	docker compose -f docker-compose.dev.yml -f docker-compose.prod.yml up --build -d