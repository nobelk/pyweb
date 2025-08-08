# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Running the Application
```bash
# Development server with hot reload
uv run fastapi dev src/main.py

# Production server via entry point
uv run pyweb --port 8000 --workers 2

# Direct execution with Python
python -m src.main --port 8000 --workers 2
```

### Package Management
```bash
# Install dependencies
uv sync

# Install with locked versions (recommended)
uv sync --locked

# Install with dev dependencies (for testing and linting)
uv sync --group dev

# Build package
uv build
```

### Testing
```bash
# Run all tests
uv run pytest

# Run tests with verbose output
uv run pytest -v

# Run specific test file
uv run pytest tests/test_health.py

# Run tests with coverage
uv run pytest --cov=src --cov-report=term-missing
```

### Docker
```bash
# Build image
docker build -t pyweb .

# Run container
docker run -p 8000:8000 pyweb

# Using docker-compose
docker-compose up -d
```

## Architecture Overview

This is a minimal FastAPI web service using modern Python tooling:

- **Framework**: FastAPI with Uvicorn ASGI server
- **Package Manager**: UV (not pip)
- **Python Version**: 3.13.4+
- **Structure**: src-layout with single module (`src/main.py`)
- **Entry Point**: CLI with argparse for `--port` and `--workers` configuration
- **Current API**: Single `/health` endpoint returning `{"status":"ok"}`

The application architecture in `src/main.py`:
1. FastAPI app instance created globally
2. `main()` function sets up argparse CLI and runs Uvicorn server
3. Uvicorn configured to bind to `0.0.0.0` with configurable port and workers

## Project Structure
```
pyweb/
├── src/
│   ├── __init__.py
│   └── main.py           # FastAPI application with CLI entry point
├── tests/
│   ├── __init__.py
│   └── test_health.py    # Unit tests for health endpoint
├── Dockerfile            # Multi-stage build using UV
├── docker-compose.yml    # Docker Compose configuration with health checks
├── pyproject.toml        # Project metadata and dependencies
├── uv.lock              # Locked dependencies
├── CLAUDE.md            # This file
└── README.md            # Project documentation
```

## Testing

The project uses **pytest** for unit testing:
- Test framework: pytest with pytest-asyncio for async support
- Test client: FastAPI TestClient for endpoint testing
- Coverage: Available via pytest-cov (install separately if needed)
- Test location: `tests/` directory

Current test coverage includes:
- Health endpoint functionality
- Response content type validation
- HTTP method validation
- 404 error handling

## Development Gaps
- **Code Quality**: Ruff is in dev dependencies but no configuration file
- **Type Checking**: No mypy or type checking setup
- **Pre-commit Hooks**: No pre-commit configuration
- **CI/CD**: No GitHub Actions or other CI/CD pipeline
- **Environment Variables**: No .env file handling or configuration management
- **Logging**: No structured logging configuration
- **API Documentation**: Only default FastAPI docs, no additional OpenAPI customization
- **Test Coverage**: Only health endpoint tested, no coverage for CLI arguments or main function