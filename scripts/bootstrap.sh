#!/usr/bin/env bash

# This file is just running all scripts in the bootstrap folder
SCRIPT_FILES="$(ls scripts/_bootstrap/*)"
for script in $SCRIPT_FILES
do
  bash $script
done
