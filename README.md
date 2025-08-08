# pyweb

A minimal FastAPI-based production-ready web service boilerplate/template built with modern Python tooling.

## 🚀 Technology Stack

- **Python 3.13.4** - Modern Python runtime
- **FastAPI** - High-performance web framework for building APIs
- **Uvicorn** - Lightning-fast ASGI server
- **UV** - Fast Python package manager (replaces pip)

## 📋 Prerequisites

- Python 3.13.4 (specified in `.python-version`)
- [UV package manager](https://github.com/astral-sh/uv)
  ```bash
  # Install UV (macOS/Linux)
  curl -LsSf https://astral.sh/uv/install.sh | sh
  
  # Install UV (Windows)
  powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd pyweb
   ```

2. Install dependencies:
   ```bash
   # Install with locked versions (recommended)
   uv sync --locked
   
   # Or install latest compatible versions
   uv sync
   ```

## ▶️ Running the Application

### Development Server (with hot reload)
```bash
# FastAPI development server with auto-reload
uv run fastapi dev --app app src/main.py
```

### Production Server
```bash
# Using the installed entry point
uv run pyweb --port 8000 --workers 2

# Or with custom configuration
uv run pyweb --port 3000 --workers 4
```

### Direct Python Execution
```bash
# Run directly with Python
python -m src.main --port 8000 --workers 2

# Or from the src directory
cd src && python main.py --port 8000 --workers 2
```

### Available CLI Arguments
- `--port`: Server port (default: 8000)
- `--workers`: Number of worker processes (default: 2)

## 📦 Building the Package

Build distribution packages (wheel and source):
```bash
uv build
```

This creates:
- `dist/*.whl` - Wheel package for distribution
- `dist/*.tar.gz` - Source distribution

## 🧹 Linting

This project uses **Ruff** for fast Python linting and formatting.

### Install Development Dependencies
```bash
# Install Ruff and other dev dependencies
uv sync --group dev
```

### Running Linting
```bash
# Check for linting issues
uv run ruff check src/

# Check with auto-fix for safe fixes
uv run ruff check --fix src/

# Check and show detailed error explanations
uv run ruff check --show-fixes src/
```

### Code Formatting
```bash
# Format code
uv run ruff format src/

# Check formatting without making changes
uv run ruff format --check src/
```

### Watch Mode (for development)
```bash
# Watch for changes and auto-check
uv run ruff check --watch src/
```

## 🧪 Testing

The project uses **pytest** for unit testing with support for async operations.

### Install Testing Dependencies
```bash
# Testing dependencies are already included in dev dependencies
uv sync --group dev
```

### Running Tests
```bash
# Run all tests
uv run pytest

# Run tests with verbose output
uv run pytest -v

# Run tests with coverage report
uv run pytest --cov=src --cov-report=term-missing

# Run specific test file
uv run pytest tests/test_health.py

# Run tests matching a pattern
uv run pytest -k "health"

# Run tests and stop on first failure
uv run pytest -x
```

### Test Structure
```
tests/
├── __init__.py
└── test_health.py    # Tests for health check endpoint
```

### Available Test Cases
- `test_health_endpoint` - Verifies the health endpoint returns correct status
- `test_health_endpoint_content_type` - Checks response content type
- `test_health_endpoint_method_not_allowed` - Tests invalid HTTP methods
- `test_nonexistent_endpoint` - Verifies 404 handling

## 🐳 Docker

### Building the Docker Image
```bash
# Build the image
docker build -t pyweb .

# Build with custom tag
docker build -t pyweb:latest .

# Build for specific platform
docker build --platform linux/amd64 -t pyweb:amd64 .
```

### Detecting vulnerabilities
```bash
docker scout quickview
```

### Running the Container
```bash
# Run with default settings (port 8000, 2 workers)
docker run -p 8000:8000 pyweb

# Run with custom port mapping
docker run -p 3000:8000 pyweb

# Run in detached mode with container name
docker run -d --name pyweb-api -p 8000:8000 pyweb

# Run with environment variables (if needed)
docker run -d --name pyweb-api -p 8000:8000 -e ENV_VAR=value pyweb

# View logs
docker logs pyweb-api

# Follow logs in real-time
docker logs -f pyweb-api

# Stop the container
docker stop pyweb-api

# Remove the container
docker rm pyweb-api
```

### Testing the Container
```bash
# Health check endpoint
curl http://localhost:8000/health
# Expected response: {"status": "ok"}

# View API documentation (when running)
# Open browser to: http://localhost:8000/docs
```

### Docker Compose
A `docker-compose.yml` file is provided for easier container management:

```bash
# Build and start the service
docker-compose up -d

# Build without cache
docker-compose build --no-cache

# Start existing containers
docker-compose start

# Stop running containers
docker-compose stop

# View logs
docker-compose logs -f

# Remove containers and networks
docker-compose down

# Remove containers, networks, and images
docker-compose down --rmi all

# Scale the service (run multiple instances)
docker-compose up -d --scale pyweb=3
```

The docker-compose.yml includes:
- Automatic image building from Dockerfile
- Health check configuration
- Restart policy
- Environment variables for PORT and WORKERS
- Isolated network for the service

### Dockerfile Details
The Dockerfile uses a multi-stage build for efficiency:
1. **Builder stage**: Uses UV to export dependencies from `uv.lock` to `requirements.txt`
2. **Final stage**: Slim Python 3.13 image with only runtime dependencies installed via pip

This approach ensures:
- Fast builds with UV's dependency resolution
- Small final image size (~150MB)
- Consistent dependencies from the lock file
- Production-ready container with Uvicorn server

## 📚 API Documentation

### Available Endpoints

- `GET /health` - Health check endpoint
  - Returns: `{"status": "ok"}`

### Interactive API Documentation

Once the server is running, access the auto-generated documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 📁 Project Structure

```
pyweb/
├── src/                    # Source code
│   ├── __init__.py         # Package initialization
│   └── main.py             # FastAPI application and entry point
├── tests/                  # Test directory (currently empty)
│   └── __init__.py
├── Dockerfile              # Multi-stage Docker build
├── pyproject.toml          # Project configuration and dependencies
├── uv.lock                 # Locked dependency versions
├── .python-version         # Python version specification (3.13.4)
├── README.md               # This file
├── LICENSE                 # Apache License 2.0
└── CLAUDE.md               # AI assistant guidance
```

## 🔧 Configuration

The application can be configured via command-line arguments:

```python
# Default configuration in src/main.py
--port 8000      # Server port
--workers 2      # Number of Uvicorn workers
```

The server always binds to `0.0.0.0` to accept connections from any network interface.

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Ensure UV is installed
2. Install development dependencies (when configured)
3. Run linting and tests before submitting PRs
4. Follow the existing code structure and conventions