@echo off
REM Start backend server
start cmd /k "cd backend && python -m venv venv && call venv\Scripts\activate && pip install -r requirements.txt && python app.py"

REM Start frontend server
start cmd /k "cd frontend && npm install && npm start"
