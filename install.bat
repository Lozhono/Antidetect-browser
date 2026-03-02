@echo off
echo Installing dependencies...
python -m pip install -r requirements.txt
python -m camoufox fetch
echo.
echo Done! Run: python main.py
pause