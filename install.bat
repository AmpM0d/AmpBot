cd /D "%~dp0"
python -m venv .venv
.venv\Scripts\pip.exe install -r requirements.txt
.venv\Scripts\python.exe UltiBlocksAutoMod\gen_config.py