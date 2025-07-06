# Contributing to temporal-python

Thank you for your interest in contributing to temporal-python! This document provides guidelines and information for contributors.

## Code of Conduct

This project follows the [Python Community Code of Conduct](https://www.python.org/psf/conduct/). Please be respectful and inclusive in all interactions.

## Getting Started

### Development Setup

1. **Fork and clone the repository:**
   ```bash
   git clone https://github.com/yourusername/temporal-python.git
   cd temporal-python
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install development dependencies:**
   ```bash
   pip install -e ".[dev]"
   ```

4. **Install pre-commit hooks:**
   ```bash
   pre-commit install
   ```

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=temporal --cov-report=html

# Run specific test file
pytest tests/test_plain_date.py -v
```

### Code Quality

Before submitting any changes, ensure your code passes all quality checks:

```bash
# Format code
black temporal/ tests/

# Sort imports
isort temporal/ tests/

# Lint code
flake8 temporal/ tests/

# Type check
mypy temporal/

# Security check
bandit -r temporal/

# Run all checks at once (pre-commit)
pre-commit run --all-files
```

## Contributing Guidelines

### 1. JavaScript Temporal API Compatibility

This project aims to be a 1:1 port of the JavaScript Temporal API. When contributing:

- **Check the specification**: Refer to the [TC39 Temporal proposal](https://tc39.es/proposal-temporal/) for the official specification
- **Maintain compatibility**: New features should match JavaScript Temporal behavior as closely as possible
- **Python conventions**: Adapt to Python naming conventions (snake_case instead of camelCase)

### 2. Adding New Features

Before implementing a new feature:

1. **Check if it exists in JavaScript Temporal**: Verify the feature exists in the official specification
2. **Open an issue**: Discuss the feature before implementing it
3. **Follow existing patterns**: Look at similar implementations in the codebase

### 3. Code Style

- **Follow PEP 8**: Use Python standard style guidelines
- **Type hints**: All new code must include type hints
- **Docstrings**: Use clear, descriptive docstrings for all public methods
- **Comments**: Add comments for complex logic, but prefer self-documenting code

### 4. Testing

All contributions must include comprehensive tests:

- **Test coverage**: Aim for 100% test coverage for new code
- **Multiple scenarios**: Test normal cases, edge cases, and error conditions
- **Documentation tests**: Ensure examples in docstrings work correctly

Example test structure:
```python
class TestNewFeature:
    def test_basic_functionality(self):
        """Test basic usage of the new feature."""
        # Test implementation
        
    def test_edge_cases(self):
        """Test edge cases and boundary conditions."""
        # Edge case tests
        
    def test_error_conditions(self):
        """Test that appropriate errors are raised."""
        with pytest.raises(ExpectedError):
            # Error condition test
```

### 5. Documentation

- **Update README**: Add examples for new classes or significant features
- **Docstrings**: Follow the Google docstring style
- **Type hints**: Use precise type annotations
- **Examples**: Include usage examples in docstrings

## Pull Request Process

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes:**
   - Write code following the guidelines above
   - Add comprehensive tests
   - Update documentation

3. **Test your changes:**
   ```bash
   pytest tests/ -v
   pre-commit run --all-files
   ```

4. **Commit your changes:**
   ```bash
   git add .
   git commit -m "Add feature: description of what you added"
   ```

5. **Push and create PR:**
   ```bash
   git push origin feature/your-feature-name
   ```
   Then create a Pull Request on GitHub.

### PR Requirements

- [ ] All tests pass
- [ ] Code coverage is maintained or improved
- [ ] Pre-commit hooks pass
- [ ] Documentation is updated (if applicable)
- [ ] CHANGELOG.md is updated (for significant changes)
- [ ] Commit messages are clear and descriptive

## Types of Contributions

### 🐛 Bug Fixes
- Fix incorrect behavior
- Add regression tests
- Update documentation if behavior changes

### ✨ New Features
- Implement missing JavaScript Temporal API methods
- Add new classes or functionality from the specification
- Ensure full test coverage

### 📚 Documentation
- Improve README examples
- Add missing docstrings
- Fix typos or unclear explanations

### 🔧 Infrastructure
- Improve CI/CD pipelines
- Update dependencies
- Enhance development tools

## Release Process

Releases are automated through GitHub Actions when tags are pushed:

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Create and push a tag: `git tag v1.x.x && git push origin v1.x.x`
4. GitHub Actions will automatically build and publish to PyPI

## Questions?

If you have questions about contributing:

1. Check existing [issues](https://github.com/hasanatkazmi/temporal-python/issues)
2. Open a new [discussion](https://github.com/hasanatkazmi/temporal-python/discussions)
3. Refer to the [JavaScript Temporal specification](https://tc39.es/proposal-temporal/)

Thank you for contributing to temporal-python! 🎉