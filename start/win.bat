@echo off
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt -i https://mirror-pypi.runflare.com/simple
::streamlit run ui.py