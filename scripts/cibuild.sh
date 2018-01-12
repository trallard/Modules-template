#!/bin/bash
set -e # halt script on error

# The conversion of the notebooks is done via the nbjekyll package
# https://github.com/trallard/nbconvert-jekyllconvert
python -m nbjekyll.convert_nbs

# build the site and test
bundle exec jekyll build  # builds the site
bundle exec htmlproofer ./_site --disable-external --check-favicon --only_4xx # checks that there are no broke links
