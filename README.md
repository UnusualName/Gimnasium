python -m venv venv

# For Windows
venv\Scripts\activate

# For OSX and Linux
source venv/bin/activate


pip install -r requirements.txt
python lyceum\manage.py startserver