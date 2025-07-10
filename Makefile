setup:
	uv sync
	uv run lefthook install
dev:
	docker compose --env-file .env.local up --remove-orphans --build