#!/usr/bin/env bash

echo "installing required tools:"
echo "installing pipx"
pip install -U pipx
echo "using pipx to install nitpick"
pipx install nitpick
echo "installing shellcheck"
sudo apt install shellcheck
