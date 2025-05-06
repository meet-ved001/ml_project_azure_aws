@echo off

REM Create virtual environment
python -m venv venv
call venv\Scripts\activate.bat

REM Install dependencies
pip install -r requirements.txt

REM Create deployment package
if not exist deploy mkdir deploy
xcopy /E /I /Y application.py deploy\
xcopy /E /I /Y requirements.txt deploy\
xcopy /E /I /Y Procfile deploy\
xcopy /E /I /Y .ebextensions deploy\
xcopy /E /I /Y src deploy\
xcopy /E /I /Y static deploy\
xcopy /E /I /Y templates deploy\
xcopy /E /I /Y artifacts deploy\

REM Change to deploy directory and deploy
cd deploy
eb deploy student-performance-predictor-env 