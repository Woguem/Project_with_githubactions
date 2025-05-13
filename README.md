# Flask API with GitHub Actions CI/CD

A modern Flask application with comprehensive testing, Docker support, and GitHub Actions CI/CD pipeline.

## Features

- Flask application with proper project structure
- Comprehensive test suite with pytest
- Docker support with optimized Dockerfile
- GitHub Actions CI/CD pipeline
- Rate limiting and CORS support
- Logging configuration
- Health check endpoint
- Environment-based configuration

## Prerequisites

- Python 3.9+
- Docker (for containerization)
- GitHub account (for CI/CD)

## Local Development

1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
flask run
```

## Testing

Run the test suite:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=app tests/
```

## Docker

Build the Docker image:

```bash
docker build -t flasktest-app .
```

Run the container:

```bash
docker run -p 5000:5000 flasktest-app
```

## API Endpoints

- `GET /`: Welcome message
- `GET /health`: Health check endpoint
- `POST /api/echo`: Echo endpoint that returns the sent JSON data
- `GET /api/error-example`: Example error endpoint

## CI/CD Pipeline

The GitHub Actions workflow includes:

- Running tests
- Code linting
- Docker image building and publishing
- Caching for faster builds

## Environment Variables

Create a `.env` file with the following variables:

```
SECRET_KEY=your-secret-key
FLASK_ENV=development
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
