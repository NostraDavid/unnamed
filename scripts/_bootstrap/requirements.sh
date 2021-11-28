#!/usr/bin/env bash

echo "installing dev requirements"
# pip install -r requirements/dev.txt
pip install --quiet --requirement requirements/dev.txt
echo "installing application locally, in 'editable mode' as 'ctbi'"
# pip install -e .
pip install --quiet --no-deps --editable .
echo "app installed; run 'ctbi' after this script is done"
