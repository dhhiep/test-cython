#!/usr/bin/env bash

# Reset codebase
git checkout .
rm -rf build
find . -type f -name "*.so" -delete

# Install virtual environtment and install dependencies
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
poetry lock --no-update
poetry install --no-root

# Build
python compile.py build_ext --inplace

# Remove all python files except compile.py and main_launcher.py
find . -type f -name "*.py" ! -name "compile.py" ! -name "main_launcher.py" ! -name "__init__.py" -delete
rm -rf build

# Run
python main_launcher.py