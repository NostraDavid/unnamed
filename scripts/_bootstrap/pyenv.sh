#!/usr/bin/env bash

echo "Installing PyEnv, which is needed for Tox, as we're testing against multiple versions of Python."
curl --silent https://pyenv.run | bash

echo "Installing multiple python versions"
echo "If these versions get out of sync with Tox, the Tox settings are leading."
for python_version in $(cat .python-version)
do
  pyenv install $python_version
done