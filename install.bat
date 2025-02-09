cd /D "%~dp0"
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
python gen_config.py