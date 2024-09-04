#!/bin/bash

# Ensure the script exits if any command fails
set -e

# Activate the Poetry environment and run the Python script
poetry run python main.py "$@"
