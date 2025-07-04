# PyPI Upload Guide for temporal-python

## 📦 Package Ready for Upload

Your `temporal-python` package v0.0.1 is built and ready for PyPI upload!

**Package files:**
- ✅ `temporal_python-0.0.1-py3-none-any.whl` (wheel)
- ✅ `temporal_python-0.0.1.tar.gz` (source distribution)
- ✅ All validation checks passed
- ✅ Local installation tested successfully

## 🔑 Step 1: Get PyPI API Token

1. Go to [PyPI Account Settings](https://pypi.org/manage/account/)
2. Click "Add API token"
3. Give it a name like "temporal-python-upload"
4. Set scope to "Entire account" (or specific project if you prefer)
5. Copy the generated token (starts with `pypi-`)

## 🧪 Step 2: Test Upload (Recommended)

Test on TestPyPI first to make sure everything works:

```bash
# Upload to TestPyPI first
source pypi_env/bin/activate
twine upload --repository testpypi dist/*
# Username: __token__
# Password: [your TestPyPI API token]

# Test installation from TestPyPI
pip install --index-url https://test.pypi.org/simple/ temporal-python
```

## 🚀 Step 3: Upload to PyPI

### Option A: Using Environment Variables (Recommended)

```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pypi-your-api-token-here
./upload_to_pypi.sh
```

### Option B: Interactive Upload

```bash
./upload_to_pypi.sh
# When prompted:
# Username: __token__
# Password: [paste your API token]
```

### Option C: Manual Commands

```bash
source pypi_env/bin/activate
twine upload dist/*
```

## ✅ Step 4: Verify Upload

After successful upload:

1. **Check PyPI page**: https://pypi.org/project/temporal-python/
2. **Test installation**: `pip install temporal-python`
3. **Test import**: `python -c "import temporal; print(temporal.__version__)"`

## 📋 Package Information

- **Name**: `temporal-python`
- **Version**: `0.0.1`
- **Import**: `import temporal`
- **GitHub**: https://github.com/hasanatkazmi/temporal-python
- **License**: MIT
- **Python**: 3.7+

## 🔧 Troubleshooting

### Authentication Issues
- Make sure username is exactly `__token__`
- API token should start with `pypi-`
- Token must have upload permissions

### Package Already Exists
- Each version can only be uploaded once
- Increment version in `pyproject.toml` and `temporal/__init__.py`
- Rebuild with `python -m build`

### Upload Failures
- Check network connection
- Verify package passes `twine check dist/*`
- Ensure all required files are included

## 🎉 After Upload

Once uploaded successfully:

```bash
# Anyone can install your package with:
pip install temporal-python

# And use it like:
python -c "
from temporal import PlainDate, Duration
date = PlainDate(2023, 6, 15)
result = date.add(Duration(days=7))
print(f'{date} + 7 days = {result}')
"
```

Your package will be available at: https://pypi.org/project/temporal-python/