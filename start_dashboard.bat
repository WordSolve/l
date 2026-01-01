@echo off
REM RedCode Quantum Miner Dashboard Startup Script for Windows
REM Chocolatey Integration for Smooth Operation

echo ==========================================
echo RedCode Quantum Miner Dashboard
echo Chocolatey Package Manager Integration
echo ==========================================
echo.

REM Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo.
    echo Would you like to install dependencies using Chocolatey?
    echo This will install Python and all required packages automatically.
    echo.
    choice /C YN /M "Run Chocolatey installation script"
    if errorlevel 2 goto :nochoco
    if errorlevel 1 goto :installchoco
    
    :installchoco
    echo.
    echo Running Chocolatey installation...
    powershell -ExecutionPolicy Bypass -File chocolatey_install.ps1
    echo.
    echo Please restart this script after installation completes.
    pause
    exit /b 0
    
    :nochoco
    echo.
    echo Please install Python 3.8 or higher manually:
    echo https://www.python.org/downloads/
    echo.
    echo Or run: chocolatey_install.ps1
    pause
    exit /b 1
)

echo Checking dependencies...
python -c "import numpy" >nul 2>&1
if errorlevel 1 (
    echo NumPy not found. Installing dependencies...
    pip install -r requirements.txt
)

python -c "import requests" >nul 2>&1
if errorlevel 1 (
    echo Requests not found. Installing dependencies...
    pip install -r requirements.txt
)

echo.
echo All dependencies verified!
echo.
echo Starting RedCode Quantum Miner Dashboard...
echo.

REM Launch the dashboard
python miner_dashboard_ui.py

if errorlevel 1 (
    echo.
    echo Dashboard encountered an error
    echo.
    echo Troubleshooting:
    echo 1. Check that all dependencies are installed: pip list
    echo 2. Review config.json for correct settings
    echo 3. See CHOCOLATEY_SETUP.md for installation help
    echo.
    pause
    exit /b 1
)

echo.
echo Dashboard closed successfully
pause
