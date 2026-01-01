# Chocolatey Setup Guide for RedCode Quantum Miner Dashboard

This guide covers the automated Windows setup using Chocolatey package manager for smooth installation and operation.

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Automated Installation](#automated-installation)
4. [Manual Installation](#manual-installation)
5. [Package Details](#package-details)
6. [Troubleshooting](#troubleshooting)
7. [Uninstallation](#uninstallation)

---

## Overview

The RedCode Quantum Miner Dashboard includes **Chocolatey integration** for Windows to automate installation of all dependencies:

- **Python 3.11+** - Core runtime environment
- **NumPy** - Numerical computing for quantum algorithms
- **Requests** - HTTP library for live price fetching
- **Git** - Version control (optional but recommended)
- **Visual C++ Redistributables** - Required for compiled Python packages

### Why Chocolatey?

✅ **Automated Installation** - One script installs everything  
✅ **Dependency Management** - Handles version conflicts  
✅ **Silent Updates** - Easy package updates  
✅ **Clean Uninstall** - Complete removal when needed  
✅ **Standard Approach** - Industry-standard Windows package manager

---

## Prerequisites

### System Requirements

- **Windows 10/11** (64-bit recommended)
- **PowerShell 5.1+** or **PowerShell Core 7+**
- **Administrator privileges** (required for Chocolatey installation)
- **Internet connection** (for downloading packages)

### Before You Begin

1. **Close all applications** to avoid file locks
2. **Disable antivirus temporarily** if it blocks PowerShell scripts
3. **Backup your config.json** if you have existing settings

---

## Automated Installation

### Step 1: Run Chocolatey Installation Script

**Option A: Using PowerShell (Recommended)**

1. **Right-click** on the Start menu
2. Select **"Windows PowerShell (Admin)"** or **"Terminal (Admin)"**
3. Navigate to the dashboard directory:
   ```powershell
   cd C:\path\to\l
   ```
4. Run the installation script:
   ```powershell
   .\chocolatey_install.ps1
   ```

**Option B: Using File Explorer**

1. Navigate to the dashboard folder
2. **Right-click** on `chocolatey_install.ps1`
3. Select **"Run with PowerShell"**
4. Allow Administrator privileges when prompted

### Step 2: Follow On-Screen Prompts

The script will:

1. ✅ Check if Chocolatey is installed (install if missing)
2. ✅ Verify Python 3.8+ is present (install Python 3.11 if needed)
3. ✅ Install Git for repository management
4. ✅ Install Visual C++ Redistributables
5. ✅ Install Python dependencies from `requirements.txt`
6. ✅ Optionally install Monero GUI Wallet
7. ✅ Optionally install Tari wallet dependencies

### Step 3: Verify Installation

```powershell
# Check Chocolatey
choco --version

# Check Python
python --version

# Check installed packages
pip list
```

Expected output:
```
Chocolatey v2.x.x
Python 3.11.x
numpy         1.24.0
requests      2.31.0
```

---

## Manual Installation

If you prefer manual setup or the automated script fails:

### 1. Install Chocolatey

Open PowerShell as Administrator and run:

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

### 2. Install Python

```powershell
choco install python --version=3.11.0 -y
```

### 3. Install Git (Optional)

```powershell
choco install git -y
```

### 4. Install Visual C++ Redistributables

```powershell
choco install vcredist-all -y
```

### 5. Install Python Dependencies

```powershell
cd C:\path\to\l
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 6. Verify Installation

```powershell
python test_dashboard.py
```

---

## Package Details

### Core Packages Installed

| Package | Version | Purpose |
|---------|---------|---------|
| **Chocolatey** | Latest | Windows package manager |
| **Python** | 3.11.0+ | Core runtime |
| **pip** | Latest | Python package manager |
| **numpy** | 1.24.0+ | Quantum algorithm computations |
| **requests** | 2.31.0+ | Live price API calls |
| **Git** | Latest | Repository management |
| **vcredist-all** | Latest | Visual C++ dependencies |

### Optional Packages

| Package | Purpose |
|---------|---------|
| **Monero GUI** | Monero wallet integration with GhostRider |
| **Tari Wallet** | Tari CLI for one-sided payment flow |

---

## Troubleshooting

### Issue: "Running scripts is disabled on this system"

**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then rerun the installation script.

### Issue: "Chocolatey is not recognized"

**Solution:**
Close and reopen PowerShell to refresh environment variables, or manually add to PATH:

```powershell
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
```

### Issue: Python package installation fails

**Solution:**
Upgrade pip and retry:
```powershell
python -m pip install --upgrade pip
pip install --upgrade setuptools wheel
pip install -r requirements.txt
```

### Issue: NumPy installation error on ARM64

**Solution:**
Use alternative NumPy build:
```powershell
pip install numpy --only-binary :all:
```

### Issue: Antivirus blocks installation

**Solution:**
Temporarily disable antivirus or add exceptions for:
- `C:\ProgramData\chocolatey\`
- `C:\Python311\`
- Your dashboard directory

### Issue: "Access Denied" during installation

**Solution:**
Ensure PowerShell is running as Administrator. Check by running:
```powershell
([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
```

Should return `True`.

---

## Uninstallation

### Remove Dashboard Dependencies

```powershell
# Remove Python packages
pip uninstall numpy requests -y

# Remove Python (optional)
choco uninstall python -y

# Remove Git (optional)
choco uninstall git -y
```

### Remove Chocolatey (Optional)

```powershell
# Run in PowerShell as Administrator
Remove-Item C:\ProgramData\chocolatey -Recurse -Force
```

### Clean Dashboard Files

Simply delete the dashboard folder after uninstalling dependencies.

---

## Advanced Configuration

### Using Chocolatey for Updates

Keep all packages updated:

```powershell
# Update Chocolatey itself
choco upgrade chocolatey -y

# Update Python
choco upgrade python -y

# Update all packages
choco upgrade all -y

# Update Python dependencies
pip install --upgrade -r requirements.txt
```

### Silent Installation for Automated Deployment

For batch deployment across multiple machines:

```powershell
# Run silently without prompts
.\chocolatey_install.ps1 -Unattended
```

### Creating Chocolatey Package (Advanced)

To create a Chocolatey package for the dashboard itself:

1. Create `redcode-miner-dashboard.nuspec`
2. Define dependencies and install scripts
3. Build package: `choco pack`
4. Deploy: `choco install redcode-miner-dashboard -source .`

(See Chocolatey documentation for details)

---

## Post-Installation Steps

After Chocolatey installation completes:

### 1. Configure Dashboard

Edit `config.json` to set your experiment parameters:

```json
{
  "experiment_features": {
    "real_mining_mode": false,
    "quantum_5d_strategy": false
  }
}
```

### 2. Launch Dashboard

Run the Windows launcher:

```cmd
start_dashboard.bat
```

Or directly with Python:

```powershell
python miner_dashboard_ui.py
```

### 3. Review Activation Status

The UI will show what features are **NOT ACTIVATED** (in red). See `ACTIVATION_GUIDE.md` for enabling experimental features.

### 4. Set Up Wallets (Optional)

For Monero GUI and Tari CLI integration, see `WALLET_INTEGRATION_GUIDE.md`.

---

## Support and Resources

### Official Documentation

- **README.md** - Main documentation
- **ACTIVATION_GUIDE.md** - Feature activation guide
- **WALLET_INTEGRATION_GUIDE.md** - Wallet setup guide
- **IMPLEMENTATION.md** - Technical details

### External Resources

- **Chocolatey Website**: https://chocolatey.org/
- **Python Downloads**: https://www.python.org/downloads/
- **Git for Windows**: https://git-scm.com/download/win
- **Monero GUI**: https://www.getmonero.org/downloads/
- **Tari Wallet**: https://www.tari.com/downloads/

### Common Commands Reference

```powershell
# Check installed packages
choco list --local-only

# Search for packages
choco search python

# Get package info
choco info python

# Upgrade specific package
choco upgrade python -y

# Downgrade package
choco install python --version=3.10.0 --force -y
```

---

## Summary

✅ **Automated Setup** - One script installs everything  
✅ **All Dependencies Managed** - Python, NumPy, Requests, VC++ Redist  
✅ **Easy Updates** - Simple command to update all packages  
✅ **Clean Uninstall** - Remove everything with Chocolatey  
✅ **Windows Optimized** - Designed for smooth Windows operation

The Chocolatey integration ensures that the RedCode Quantum Miner Dashboard runs smoothly on Windows with minimal manual configuration.

**Ready to start?** Run `.\chocolatey_install.ps1` and launch your experiments!
