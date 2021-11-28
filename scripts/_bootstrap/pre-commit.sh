#!/usr/bin/env bash

echo "installing pre-commit scripts into git, so you don't need to fix things AFTER you commit :)"
PRE_COMMIT_VERSION=$(grep --only-matching --perl-regexp "pre-commit==\d+\.\d+\.\d+" ./requirements/dev.txt)
pip install --quiet "$PRE_COMMIT_VERSION"
pre-commit install
