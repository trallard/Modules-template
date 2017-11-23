#!/bin/bash
clear
echo "Converting notebooks now"

jupyter nbconvert --config scripts/nb_jekyll.py

python scripts/nb_replace.py

echo "Notebooks ready"
