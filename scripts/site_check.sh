#!/usr/bin/env bash
set -e # halt script on error

bundle exec jekyll build  # builds the site
bundle exec htmlproofer ./_site --disable-external --check-favicon --only_4xx --ignore-file "/presentation/"# checks that there are no broken links 
