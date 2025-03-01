#!/bin/bash
cd "$(dirname $0)"
python -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python AmpBot/gen_config.py
sh gen_start_scripts.sh
