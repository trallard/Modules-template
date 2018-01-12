#!/bin/bash
set -e

TARGET_BRANCH='master'

# Save some useful information
REPO=`git config remote.origin.url`
SSH_REPO=${REPO/https:\/\/github.com\//git@github.com:}
SHA=`git rev-parse --verify HEAD`

# Add the changes
git add .
git commit -m "Site checked and NB converted on Travis $TRAVIS_BUILD"
