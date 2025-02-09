#!/bin/bash
cd "$(dirname $0)"
python -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python gen_config.py
