@echo off
REM Activate virtual environment
call venv\Scripts\activate

REM Update pip
python -m pip install --upgrade pip

REM Install required packages
pip install -r requirements.txt

REM Run the backend server
python app.py
