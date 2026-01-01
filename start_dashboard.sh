#!/bin/bash
# RedCode Quantum Miner Dashboard Startup Script

echo "=========================================="
echo "RedCode Quantum Miner Dashboard"
echo "=========================================="
echo ""

# Check Python version
PYTHON_VERSION=$(python3 --version 2>&1 | grep -Po '(?<=Python )\d+\.\d+')
REQUIRED_VERSION="3.8"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo "Error: Python 3.8 or higher is required"
    echo "Current version: $PYTHON_VERSION"
    exit 1
fi

echo "✓ Python version: $PYTHON_VERSION"
echo ""

# Check if requirements are installed
echo "Checking dependencies..."
if python3 -c "import numpy" 2>/dev/null; then
    echo "✓ NumPy installed"
else
    echo "Installing dependencies..."
    pip install -r requirements.txt
fi

echo ""
echo "Starting RedCode Quantum Miner Dashboard..."
echo ""

# Launch the dashboard
python3 miner_dashboard_ui.py

# Check exit status
if [ $? -eq 0 ]; then
    echo ""
    echo "Dashboard closed successfully"
else
    echo ""
    echo "Dashboard encountered an error"
    exit 1
fi
