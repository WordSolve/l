# RedCode Quantum Miner Dashboard - Chocolatey Installation Script
# This script automates the installation of all dependencies using Chocolatey

Write-Host "========================================"
Write-Host "RedCode Quantum Miner Dashboard Setup"
Write-Host "Chocolatey Package Manager Integration"
Write-Host "========================================"
Write-Host ""

# Check if running as Administrator
$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
$isAdmin = $currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "ERROR: This script must be run as Administrator" -ForegroundColor Red
    Write-Host "Right-click PowerShell and select 'Run as Administrator'" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

# Function to check if Chocolatey is installed
function Test-ChocolateyInstalled {
    try {
        $chocoVersion = choco --version 2>$null
        return $true
    }
    catch {
        return $false
    }
}

# Install Chocolatey if not present
if (-not (Test-ChocolateyInstalled)) {
    Write-Host "Chocolatey not found. Installing Chocolatey..." -ForegroundColor Yellow
    Write-Host ""
    
    Set-ExecutionPolicy Bypass -Scope Process -Force
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
    
    try {
        Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
        Write-Host "Chocolatey installed successfully!" -ForegroundColor Green
        Write-Host ""
        
        # Refresh environment variables
        $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
    }
    catch {
        Write-Host "ERROR: Failed to install Chocolatey" -ForegroundColor Red
        Write-Host $_.Exception.Message
        Read-Host "Press Enter to exit"
        exit 1
    }
}
else {
    Write-Host "Chocolatey is already installed (Version: $(choco --version))" -ForegroundColor Green
    Write-Host ""
}

# Install Python if not present
Write-Host "Checking Python installation..." -ForegroundColor Cyan
try {
    $pythonVersion = python --version 2>&1
    if ($pythonVersion -match "Python (\d+)\.(\d+)") {
        $major = [int]$matches[1]
        $minor = [int]$matches[2]
        
        if ($major -ge 3 -and $minor -ge 8) {
            Write-Host "Python $pythonVersion is already installed" -ForegroundColor Green
        }
        else {
            Write-Host "Python version too old. Installing Python 3.11..." -ForegroundColor Yellow
            choco install python --version=3.11.0 -y
        }
    }
}
catch {
    Write-Host "Python not found. Installing Python 3.11..." -ForegroundColor Yellow
    choco install python --version=3.11.0 -y
}
Write-Host ""

# Refresh environment after Python installation
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# Install Git (useful for repository management)
Write-Host "Checking Git installation..." -ForegroundColor Cyan
try {
    $gitVersion = git --version 2>&1
    Write-Host "Git is already installed: $gitVersion" -ForegroundColor Green
}
catch {
    Write-Host "Git not found. Installing Git..." -ForegroundColor Yellow
    choco install git -y
}
Write-Host ""

# Install Visual C++ Redistributables (required for some Python packages)
Write-Host "Checking Visual C++ Redistributables..." -ForegroundColor Cyan
choco install vcredist-all -y
Write-Host ""

# Install Python dependencies
Write-Host "Installing Python dependencies..." -ForegroundColor Cyan
Write-Host ""

$requirementsPath = Join-Path $PSScriptRoot "requirements.txt"
if (Test-Path $requirementsPath) {
    python -m pip install --upgrade pip
    python -m pip install -r $requirementsPath
    Write-Host "Python dependencies installed successfully!" -ForegroundColor Green
}
else {
    Write-Host "WARNING: requirements.txt not found in script directory" -ForegroundColor Yellow
    Write-Host "Installing core dependencies manually..." -ForegroundColor Yellow
    python -m pip install --upgrade pip
    python -m pip install numpy>=1.24.0
    python -m pip install requests>=2.31.0
}
Write-Host ""

# Optional: Install Monero GUI Wallet
Write-Host "Optional: Install Monero GUI Wallet for wallet integration?" -ForegroundColor Cyan
$installMonero = Read-Host "Install Monero GUI? (y/N)"
if ($installMonero -eq "y" -or $installMonero -eq "Y") {
    Write-Host "Installing Monero GUI Wallet..." -ForegroundColor Yellow
    # Note: Monero GUI may not be in official Chocolatey repo, manual download recommended
    Write-Host "Please download Monero GUI manually from: https://www.getmonero.org/downloads/" -ForegroundColor Yellow
    Write-Host ""
}

# Optional: Install Tari dependencies
Write-Host "Optional: Install Tari console wallet for flow pushing?" -ForegroundColor Cyan
$installTari = Read-Host "Install Tari dependencies? (y/N)"
if ($installTari -eq "y" -or $installTari -eq "Y") {
    Write-Host "Installing Tari dependencies..." -ForegroundColor Yellow
    Write-Host "Please download Tari wallet from: https://www.tari.com/downloads/" -ForegroundColor Yellow
    Write-Host ""
}

Write-Host "========================================"
Write-Host "Installation Complete!" -ForegroundColor Green
Write-Host "========================================"
Write-Host ""
Write-Host "All dependencies have been installed using Chocolatey."
Write-Host ""
Write-Host "Next Steps:" -ForegroundColor Cyan
Write-Host "1. Review and edit config.json for your experiment settings"
Write-Host "2. Run start_dashboard.bat to launch the dashboard"
Write-Host "3. See ACTIVATION_GUIDE.md for enabling experimental features"
Write-Host ""
Write-Host "For wallet integration:"
Write-Host "- Monero GUI: See WALLET_INTEGRATION_GUIDE.md"
Write-Host "- Tari CLI: See WALLET_INTEGRATION_GUIDE.md"
Write-Host ""
Read-Host "Press Enter to exit"
