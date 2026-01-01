@echo off
REM RedCode Quantum Miner Dashboard Startup Script for Windows

echo ==========================================
echo RedCode Quantum Miner Dashboard
echo ==========================================
echo.

REM Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

echo Checking dependencies...
python -c "import numpy" >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements.txt
)

echo.
echo Starting RedCode Quantum Miner Dashboard...
echo.

REM Launch the dashboard
python miner_dashboard_ui.py

if errorlevel 1 (
    echo.
    echo Dashboard encountered an error
    pause
    exit /b 1
)

echo.
echo Dashboard closed successfully
pause
