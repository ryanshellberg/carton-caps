FROM public.ecr.aws/docker/library/debian:bookworm-slim

# Install uv package manger from their distroless docker image.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Install dependencies. Doing this first so that we can cache the dependencies between builds unless the uv.lock file changes.
COPY pyproject.toml uv.lock .python-version /app/
WORKDIR /app

# The default link mode is hardlinks, which doesn't work because the cache is a mounted volume, i.e. a different filesystem.
ENV UV_LINK_MODE=copy
RUN --mount=type=cache,target=/root/.cache/uv uv sync --no-dev --frozen --compile-bytecode

# Copy the rest of the project.
COPY . /app

# Compile the rest of the project.
RUN --mount=type=cache,target=/root/.cache/uv uv sync --no-dev --frozen --compile-bytecode

# Expose the server port.
EXPOSE 8000

CMD ["uv", "run", "--no-dev", "uvicorn", "service:app", "--app-dir", "src", "--host", "0.0.0.0", "--port", "8000"]