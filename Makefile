.PHONY: build up down logs clean test lint help

# Default target
help:
	@echo "Available commands:"
	@echo "  make build    - Build all Docker containers"
	@echo "  make up       - Start all containers in detached mode"
	@echo "  make down     - Stop and remove all containers"
	@echo "  make logs     - View logs from all containers"
	@echo "  make clean    - Remove all containers and volumes"
	@echo "  make test     - Run tests"
	@echo "  make lint     - Run linting"

# Build containers
build:
	docker-compose build

# Start containers
up:
	docker-compose up -d

# Stop containers
down:
	docker-compose down

# View logs
logs:
	docker-compose logs -f

# Clean up containers and volumes
clean:
	docker-compose down -v
	docker system prune -f

# Run tests
test:
	docker-compose run --rm backend pytest

# Run linting
lint:
	docker-compose run --rm backend flake8
	docker-compose run --rm backend black --check . 