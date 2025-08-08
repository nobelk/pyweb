# Use UV image that includes Python 3.13
FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR /app

# Install curl for health checks
RUN apt-get update && apt-get install -y curl && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY pyproject.toml uv.lock ./

# Install dependencies using UV
RUN uv sync --frozen --no-dev

# Copy the source code
COPY src /app/src

# Run the application using UV
CMD ["uv", "run", "python", "-m", "src.main", "--port", "8000", "--workers", "2"]
