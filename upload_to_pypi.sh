#!/bin/bash

# PyPI Upload Script for temporal-python
# Run this script to upload your package to PyPI

echo "🚀 Uploading temporal-python v0.0.1 to PyPI..."
echo ""

# Check if dist files exist
if [ ! -f "dist/temporal_python-0.0.1-py3-none-any.whl" ]; then
    echo "❌ Error: Distribution files not found. Run 'python -m build' first."
    exit 1
fi

# Activate virtual environment
echo "📝 Activating virtual environment..."
source pypi_env/bin/activate

# Verify package
echo "🔍 Checking package..."
twine check dist/*

if [ $? -ne 0 ]; then
    echo "❌ Package check failed. Please fix issues before uploading."
    exit 1
fi

echo ""
echo "✅ Package validation passed!"
echo ""

# Check if environment variables are set
if [ -n "$TWINE_USERNAME" ] && [ -n "$TWINE_PASSWORD" ]; then
    echo "🔑 Using environment variables for authentication..."
    twine upload dist/*
else
    echo "🔑 No environment variables found. You'll be prompted for credentials..."
    echo "   Username: __token__"
    echo "   Password: [your PyPI API token]"
    echo ""
    twine upload dist/*
fi

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 Successfully uploaded temporal-python v0.0.1 to PyPI!"
    echo "📦 Package URL: https://pypi.org/project/temporal-python/"
    echo "💾 Install with: pip install temporal-python"
else
    echo ""
    echo "❌ Upload failed. Please check your credentials and try again."
    exit 1
fi