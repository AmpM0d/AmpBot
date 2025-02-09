#!/bin/sh
cd "$(dirname $0)"
. .venv/bin/activate
python sandboxbot.py &
python remindmebot.py &
