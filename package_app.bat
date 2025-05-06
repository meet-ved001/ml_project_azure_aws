@echo off

REM Create a clean directory for packaging
if exist "deploy" rmdir /s /q "deploy"
mkdir deploy

REM Copy all necessary files
xcopy /E /I /Y application.py deploy\
xcopy /E /I /Y requirements.txt deploy\
xcopy /E /I /Y Procfile deploy\
xcopy /E /I /Y .ebextensions deploy\
xcopy /E /I /Y src deploy\
xcopy /E /I /Y static deploy\
xcopy /E /I /Y templates deploy\
xcopy /E /I /Y artifacts deploy\

REM Create a ZIP file
powershell Compress-Archive -Path deploy\* -DestinationPath student-performance-app.zip -Force

echo Application packaged successfully as student-performance-app.zip
pause 