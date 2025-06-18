"""
Setup script for the Python Temporal API.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="python-temporal",
    version="0.1.0",
    author="Temporal API Contributors",
    author_email="temporal@example.com",
    description="A Python port of JavaScript's Temporal API for modern date and time handling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/example/python-temporal",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
    install_requires=[
        "backports.zoneinfo; python_version<'3.9'",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov",
            "black",
            "flake8",
        ],
    },
    keywords="temporal, date, time, datetime, calendar, timezone, duration",
    project_urls={
        "Bug Tracker": "https://github.com/example/python-temporal/issues",
        "Documentation": "https://python-temporal.readthedocs.io/",
        "Source Code": "https://github.com/example/python-temporal",
    },
)
