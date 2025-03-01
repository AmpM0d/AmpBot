#!/bin/sh
# Go to the project's root directory
cd "$(dirname $0)"
# Run the bot, with any arguments, using the virtual environment's Python.
.venv/bin/python -m AmpBot $@