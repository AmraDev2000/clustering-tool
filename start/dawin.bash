#! bin/bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt -i https://mirror-pypi.runflare.com/simple
streamlit run ui.py