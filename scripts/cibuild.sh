#!/bin/bash
# Using nbval with the notebooks
echo "***** Testing notebooks"
py.test --nbval-lax */*.ipynb

echo "***** Parsing notebooks for publishing"

jupyter nbconvert --config scripts/mock.py

python scripts/nb_replace.py

clear
echo "Notebooks ready"

source deactivate
