#!/bin/bash
# We use nbval to validate the notebooks and generate the
# corresponding badge for jekyll

echo "***** Testing notebooks *****"
py.test --nbval-lax */*.ipynb

echo "***** Converting notebooks to markdown"

jupyter nbconvert --config scripts/mock.py


echo "***** Final touches"
python scripts/nb_replace.py

clear
echo "Notebooks ready"

source deactivate
