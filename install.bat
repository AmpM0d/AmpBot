cd /D "%~dp0"
python -m venv .venv
.venv\Scripts\pip.exe install -r requirements.txt
.venv\Scripts\python.exe AmpBot\gen_config.py
