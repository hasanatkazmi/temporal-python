.PHONY: help install install-dev test test-cov lint format type-check security clean build publish docs

# Default target
help:
	@echo "Available targets:"
	@echo "  install       Install package in current environment"
	@echo "  install-dev   Install package with development dependencies"
	@echo "  test          Run tests"
	@echo "  test-cov      Run tests with coverage report"
	@echo "  lint          Run linting (flake8)"
	@echo "  format        Format code (black + isort)"
	@echo "  type-check    Run type checking (mypy)"
	@echo "  security      Run security checks (bandit + safety)"
	@echo "  qa            Run all quality assurance checks"
	@echo "  clean         Clean build artifacts"
	@echo "  build         Build package"
	@echo "  publish       Publish to PyPI"
	@echo "  docs          Generate documentation"

# Installation
install:
	pip install -e .

install-dev:
	pip install -e ".[dev,test,docs]"
	pre-commit install

# Testing
test:
	pytest tests/ -v

test-cov:
	pytest tests/ -v --cov=temporal --cov-report=html --cov-report=term-missing
	@echo "Coverage report generated in htmlcov/"

test-benchmark:
	pytest tests/ -v --benchmark-only

# Code quality
lint:
	flake8 temporal/ tests/

format:
	black temporal/ tests/
	isort temporal/ tests/

type-check:
	mypy temporal/

security:
	bandit -r temporal/
	pip freeze | safety check --stdin

# Combined quality assurance
qa: format lint type-check security test

# Pre-commit
pre-commit:
	pre-commit run --all-files

# Build and publish
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: clean
	python -m build

publish: build
	twine check dist/*
	twine upload dist/*

# Documentation
docs:
	@echo "Validating README examples..."
	@python -c "
	# Test README examples
	from temporal import PlainDate, PlainYearMonth, PlainMonthDay, Duration, Instant
	
	# Test basic functionality
	date = PlainDate(2023, 6, 15)
	ym = PlainYearMonth(2023, 6)
	md = PlainMonthDay(8, 24)
	duration = Duration(days=1, hours=2)
	
	print('✅ README examples validated')
	"

# Development workflow
dev-setup: install-dev
	@echo "Development environment set up successfully!"
	@echo "Run 'make qa' to run all quality checks"

# CI simulation
ci: format lint type-check security test
	@echo "✅ All CI checks passed!"

# Release preparation
release-check:
	@echo "Checking release readiness..."
	python -c "
	import temporal
	print(f'Current version: {temporal.__version__}')
	"
	make qa
	make build
	twine check dist/*
	@echo "✅ Release ready!"