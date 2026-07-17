@echo off
echo Starting Employee Monitoring System...
echo.

REM Check if virtual environment exists
if not exist "venv\Scripts\python.exe" (
    echo Error: Virtual environment not found!
    echo Please run: python -m venv venv
    echo Then install dependencies: venv\Scripts\pip install -r backend\requirements.txt
    pause
    exit /b 1
)

REM Activate virtual environment and run
echo Activating virtual environment...
call venv\Scripts\activate.bat

if /I "%1"=="fast" goto fast

echo Starting application...
echo.
echo Access the system at: http://localhost:5000
echo Admin login: admin / admin123
echo Server login: Select 'Server' role
echo.
echo Press Ctrl+C to stop the server
echo.

python run.py

goto :eof

:fast
echo Starting in FAST MODE...
set FAST_MODE=true
set STREAM_JPEG_QUALITY=80
set FAST_STREAM_JPEG_QUALITY=45
set STREAM_FPS=24
set FAST_STREAM_WIDTH=320
set FAST_STREAM_HEIGHT=0
set STREAM_WIDTH=640
set STREAM_HEIGHT=480
set FAST_DETECTION_STRIDE=3
set FAST_MAX_GRABS=3
python run.py

pause

