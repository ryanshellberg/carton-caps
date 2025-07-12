setup:
	uv sync
	uv run lefthook install
	uv run python src/scripts/initialize_db.py
dev:
	docker compose --env-file .env.local up --remove-orphans --build

test:
	docker compose --env-file .env.local run --build --rm web uv run pytest tests/unit

integration-test:
	docker compose --env-file .env.local run --build --rm web uv run pytest tests/integration