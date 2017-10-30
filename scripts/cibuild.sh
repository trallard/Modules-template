#!/bin/bash
# Using nbval with the notebooks
py.test --nbval -lax *.ipynb
echo "Testing notebooks \n \n "

echo "+++++++++++++++ \n Parsing notebooks for publishing"

jupyter nbconvert --config scripts/nb_jekyll.py

python scripts/nb_replace.py

clear
echo "Notebooks ready"

source deactivate
