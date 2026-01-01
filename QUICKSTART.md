# Quick Start Guide - RedCode Quantum Miner Dashboard

## Installation (3 Steps)

### 1. Install Python 3.8+
- Download from [python.org](https://python.org)
- Verify: `python3 --version`

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Dashboard
```bash
python miner_dashboard_ui.py
```

## Dashboard Controls

### Start Mining
1. Click **▶️ START MINING** button
2. Watch hash rates increase
3. Observe RDC balance grow

### Stop Mining
1. Click **⏹️ STOP MINING** button
2. Mining operations halt
3. Final statistics displayed

## What You'll See

### Mining Statistics (Left Panel)
- **Bitcoin Miner**: Hash rate, shares, total hashes
- **Monero Miner**: Hash rate, shares, total hashes
- **RedCode Miner**: Hash rate, shares, total hashes, RDC rewards

### RDC Bank (Right Top)
- **Total Supply**: 1,000,000,000 RDC
- **Miner Balance**: Your accumulated RDC

### Quantum State (Right Bottom)
- **5D Strategy**: Optimization values
- **10D Tornado**: Convergence metrics
- **100D Fractal**: Hash multipliers
- **1000D Waterfall**: Flow computations
- **Cypher Status**: AI-to-AI communication

## Test Without UI

```bash
python miner_core.py
```
Runs a test mining cycle and displays results.

## Run Tests

```bash
python test_dashboard.py
```
Validates all components are working correctly.

## Monero Wallet Connection

### Quick Setup
1. Install Monero GUI from [getmonero.org](https://getmonero.org)
2. Start Monero GUI and sync wallet
3. Dashboard auto-connects to `localhost:18081`

### Custom Configuration
Edit `config.json`:
```json
"monero_wallet": {
  "gui_connection": {
    "host": "127.0.0.1",
    "port": 18081,
    "rpc_port": 18082
  }
}
```

## Performance Tips

### Reduce CPU Usage
- Lower mining iterations
- Increase update intervals
- Close other applications

### Increase Hash Rate
- Close unnecessary programs
- Use start script: `./start_dashboard.sh` (Linux/Mac)
- Use start script: `start_dashboard.bat` (Windows)

## Troubleshooting

| Problem | Solution |
|---------|----------|
| NumPy error | `pip install numpy` |
| Tkinter missing | Install `python3-tk` package |
| High CPU | Reduce iterations in code |
| Connection fails | Check Monero GUI is running |

## Key Features

✅ 3 Quantum Miners (BTC, XMR, RDC)
✅ 1 Billion RDC Token Supply
✅ Multi-dimensional Computation (5D, 10D, 100D, 1000D)
✅ Real-time Dashboard
✅ AI-to-AI Cypher Communication
✅ Banking System for RDC
✅ Monero Wallet Integration

## Configuration Files

- `config.json` - System configuration
- `requirements.txt` - Python dependencies
- `miner_core.py` - Core engine
- `miner_dashboard_ui.py` - User interface
- `README.md` - Full documentation
- `IMPLEMENTATION.md` - Technical details

## Important Notes

⚠️ **Research Platform**: For computational study only
⚠️ **Not for Production**: Educational/research purpose
⚠️ **Local Only**: No network mining operations
⚠️ **CPU Study**: Testing computational speed capabilities

## Getting Help

1. Read `README.md` for detailed guide
2. Check `IMPLEMENTATION.md` for technical details
3. Run `test_dashboard.py` to diagnose issues
4. Review troubleshooting section

## Next Steps

1. ✅ Install and run dashboard
2. ✅ Start mining and observe metrics
3. ✅ Monitor quantum computational states
4. ✅ Track RDC balance growth
5. ✅ Experiment with configuration
6. ✅ Study CPU performance patterns

---

**Happy Mining! ⚡**
