#!/usr/bin/env bash
set -e # halt script on error

bundle exec jekyll build  # builds the site
bundle exec htmlproofer --disable-external --only_4xx --file-ignore "/reveal.js/, /presentation/" ./_site # checks that there are no broken links
