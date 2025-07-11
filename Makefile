setup:
	uv sync
	uv run lefthook install
	uv run python src/scripts/initialize_db.py
dev:
	docker compose --env-file .env.local up --remove-orphans --build