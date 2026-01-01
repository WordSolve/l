# Wallet Integration Guide

Complete guide for connecting Monero GUI Wallet with GhostRider daemon and Tari CLI wallet for flow pushing.

## Table of Contents

1. [Monero GUI Wallet Integration](#monero-gui-wallet-integration)
2. [GhostRider Algorithm Support](#ghostrider-algorithm-support)
3. [Monero Daemon Connection](#monero-daemon-connection)
4. [Tari CLI Wallet Integration](#tari-cli-wallet-integration)
5. [One-Sided Payment Flow](#one-sided-payment-flow)
6. [Flow Bridge Setup](#flow-bridge-setup)
7. [Configuration Examples](#configuration-examples)
8. [Troubleshooting](#troubleshooting)

---

## Monero GUI Wallet Integration

### Prerequisites

1. **Download Monero GUI Wallet**
   - Official website: https://www.getmonero.org/downloads/
   - Choose the version for your operating system
   - Verify the download checksums

2. **Install Monero GUI**
   - Extract the downloaded archive
   - Run the Monero GUI application
   - Create or restore a wallet

### Enable RPC in Monero GUI

1. Open Monero GUI Wallet
2. Go to **Settings** → **Node**
3. Enable **Local node** (runs monerod)
4. Go to **Settings** → **Interface**
5. Enable **RPC server** on port 18082
6. Note your wallet address

### Configuration

Edit `config.json`:

```json
{
  "monero_wallet": {
    "gui_connection": {
      "enabled": true,
      "host": "127.0.0.1",
      "port": 18081,
      "rpc_port": 18082,
      "connected": false
    }
  }
}
```

### Connect from Dashboard

```python
from miner_core import MinerDashboardCore

dashboard = MinerDashboardCore()
success, message = dashboard.connect_monero_gui()
print(message)
```

---

## GhostRider Algorithm Support

### What is GhostRider?

GhostRider is a CPU-friendly mining algorithm that combines multiple cryptographic algorithms. While primarily used for other cryptocurrencies, the dashboard includes experimental support for GhostRider with Monero.

### Enable GhostRider

Edit `config.json`:

```json
{
  "monero_wallet": {
    "ghostrider": {
      "enabled": true,
      "algorithm": "GhostRider",
      "note": "Experimental GhostRider algorithm support"
    }
  }
}
```

### Features

- **Multi-algorithm**: Combines CN/R, CN/GPU, GR0-GR5 algorithms
- **CPU optimized**: Designed for CPU mining
- **Experimental**: Currently in testing phase

---

## Monero Daemon Connection

### Running Monero Daemon (monerod)

The Monero daemon is required for blockchain synchronization and mining operations.

### Start Daemon

#### Option 1: Through Monero GUI
- Monero GUI automatically starts monerod in the background
- Default port: 18081

#### Option 2: Command Line
```bash
# Start monerod
monerod --rpc-bind-port 18081 --confirm-external-bind

# With specific data directory
monerod --data-dir /path/to/monero/data --rpc-bind-port 18081
```

### Configuration

Edit `config.json`:

```json
{
  "monero_wallet": {
    "daemon_connection": {
      "enabled": true,
      "host": "127.0.0.1",
      "port": 18081
    }
  }
}
```

### Verify Connection

```python
from monero_integration import MoneroGUIConnector

monero = MoneroGUIConnector()
success, message = monero.connect_daemon()
print(message)  # Should show: "Connected to Monero daemon at block height: XXXXX"
```

---

## Tari CLI Wallet Integration

### Prerequisites

1. **Download Tari Console Wallet**
   - Official website: https://www.tari.com/downloads/
   - Choose the version for your operating system

2. **Install Tari CLI**
   - Extract the downloaded archive
   - Ensure `tari_console_wallet` is in your PATH

### Setup Tari Wallet

```bash
# Create new wallet
tari_console_wallet

# Follow the prompts to:
# - Set a password
# - Create recovery seed
# - Note your wallet address
```

### Configuration

Edit `config.json`:

```json
{
  "tari_wallet": {
    "cli_connection": {
      "enabled": true,
      "cli_path": "tari_console_wallet",
      "base_node": "127.0.0.1:18142",
      "wallet_address": ""
    }
  }
}
```

### Connect from Dashboard

```python
from miner_core import MinerDashboardCore

dashboard = MinerDashboardCore()
success, message = dashboard.connect_tari_cli()
print(message)
```

---

## One-Sided Payment Flow

### What is One-Sided Payment?

One-sided payments allow you to send Tari to a recipient without them being online. The dashboard uses this to push mining rewards to your Tari wallet automatically.

### Enable One-Sided Payments

Edit `config.json`:

```json
{
  "tari_wallet": {
    "one_sided_payments": {
      "enabled": true,
      "auto_flow": true,
      "flow_threshold": 0.1,
      "note": "Automatic flow pushing from mining to Tari wallet"
    }
  }
}
```

### Push Flow Manually

```python
from miner_core import MinerDashboardCore

dashboard = MinerDashboardCore()

# Push 0.5 XMR worth of flow to Tari
success, message = dashboard.push_flow_to_tari(0.5, source="monero")
print(message)
```

### Auto-Flow Configuration

When `auto_flow` is enabled:
- Mining rewards automatically pushed to Tari
- Triggers when balance reaches `flow_threshold`
- Uses one-sided payments for security

---

## Flow Bridge Setup

### What is Flow Bridge?

The Flow Bridge connects Monero and Tari wallets, allowing automatic transfer of mining rewards from Monero to Tari.

### Enable Flow Bridge

Edit `config.json`:

```json
{
  "flow_bridge": {
    "enabled": true,
    "monero_to_tari": {
      "enabled": true,
      "auto_transfer": true,
      "transfer_threshold": 0.5
    }
  }
}
```

### Configuration Options

- **enabled**: Master switch for flow bridge
- **auto_transfer**: Automatically transfer when threshold reached
- **transfer_threshold**: Minimum XMR balance to trigger transfer

### Manual Transfer

```python
from miner_core import MinerDashboardCore

dashboard = MinerDashboardCore()

# Transfer 1.0 XMR to Tari
success, message = dashboard.transfer_monero_to_tari(1.0)
print(message)
```

### Flow History

```python
# Get flow bridge status
status = dashboard.get_wallet_status()
flow_bridge = status['flow_bridge']

print(f"Total flows: {flow_bridge['total_flows']}")
print(f"Pending flows: {flow_bridge['pending_tari_flows']}")
```

---

## Configuration Examples

### Complete Integration Setup

```json
{
  "monero_wallet": {
    "gui_connection": {
      "enabled": true,
      "host": "127.0.0.1",
      "port": 18081,
      "rpc_port": 18082,
      "connected": false
    },
    "daemon_connection": {
      "enabled": true,
      "host": "127.0.0.1",
      "port": 18081
    },
    "ghostrider": {
      "enabled": true,
      "algorithm": "GhostRider",
      "note": "Experimental GhostRider algorithm support"
    }
  },
  "tari_wallet": {
    "cli_connection": {
      "enabled": true,
      "cli_path": "tari_console_wallet",
      "base_node": "127.0.0.1:18142",
      "wallet_address": "YOUR_TARI_ADDRESS_HERE"
    },
    "one_sided_payments": {
      "enabled": true,
      "auto_flow": true,
      "flow_threshold": 0.1
    }
  },
  "flow_bridge": {
    "enabled": true,
    "monero_to_tari": {
      "enabled": true,
      "auto_transfer": true,
      "transfer_threshold": 0.5
    }
  }
}
```

### Remote Daemon Setup

Connect to a remote Monero daemon:

```json
{
  "monero_wallet": {
    "daemon_connection": {
      "enabled": true,
      "host": "node.example.com",
      "port": 18081
    }
  }
}
```

### Testing Configuration

For testing without actual wallets:

```json
{
  "monero_wallet": {
    "gui_connection": {
      "enabled": false
    }
  },
  "tari_wallet": {
    "cli_connection": {
      "enabled": false
    }
  },
  "flow_bridge": {
    "enabled": false
  }
}
```

---

## Troubleshooting

### Monero GUI Connection Issues

**Problem**: "Cannot connect to Monero GUI wallet"

**Solutions**:
1. Ensure Monero GUI is running
2. Check RPC server is enabled in Settings
3. Verify port 18082 is not blocked
4. Check firewall settings

```bash
# Test RPC connection
curl http://127.0.0.1:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_address"}' -H 'Content-Type: application/json'
```

### Daemon Connection Issues

**Problem**: "Cannot connect to Monero daemon"

**Solutions**:
1. Ensure monerod is running
2. Check daemon is synchronized
3. Verify port 18081 is open

```bash
# Check daemon status
monerod status

# Check if daemon is listening
netstat -an | grep 18081
```

### Tari CLI Issues

**Problem**: "Tari CLI wallet not connected"

**Solutions**:
1. Verify `tari_console_wallet` is installed
2. Check PATH includes Tari binaries
3. Ensure base node is reachable

```bash
# Test Tari installation
tari_console_wallet --version

# Check base node connection
ping 127.0.0.1
```

### Flow Bridge Issues

**Problem**: "Flow bridge not initialized"

**Solutions**:
1. Enable both Monero and Tari connections
2. Set `flow_bridge.enabled` to `true`
3. Restart dashboard after config changes

```python
# Check wallet status
dashboard = MinerDashboardCore()
status = dashboard.get_wallet_status()
print(status)
```

### Port Conflicts

Common port usage:
- **18081**: Monero daemon RPC
- **18082**: Monero wallet RPC
- **18142**: Tari base node

Change ports if conflicts occur:

```json
{
  "monero_wallet": {
    "gui_connection": {
      "rpc_port": 28082
    },
    "daemon_connection": {
      "port": 28081
    }
  }
}
```

---

## API Reference

### MoneroGUIConnector

```python
from monero_integration import MoneroGUIConnector

monero = MoneroGUIConnector(host="127.0.0.1", wallet_port=18082, daemon_port=18081)

# Connect to wallet
success, message = monero.connect_wallet()

# Connect to daemon
success, message = monero.connect_daemon()

# Enable GhostRider
success, message = monero.enable_ghostrider()

# Get balance
balance = monero.get_balance()
print(f"Balance: {balance['balance']} XMR")
print(f"Unlocked: {balance['unlocked_balance']} XMR")

# Get status
status = monero.get_connection_status()
```

### TariCLIConnector

```python
from monero_integration import TariCLIConnector

tari = TariCLIConnector(cli_path="tari_console_wallet", base_node="127.0.0.1:18142")

# Connect
success, message = tari.connect()

# Push flow (one-sided payment)
success, message = tari.push_flow(0.5, source="monero")

# Get pending flows
flows = tari.get_pending_flows()

# Get status
status = tari.get_connection_status()
```

### FlowBridge

```python
from monero_integration import FlowBridge

bridge = FlowBridge(monero_connector, tari_connector)

# Transfer Monero to Tari
success, message = bridge.transfer_monero_to_tari(1.0)

# Get flow history
history = bridge.get_flow_history()

# Get bridge status
status = bridge.get_bridge_status()
```

---

## Security Considerations

### Wallet Security

1. **Never share your seed phrase**: Keep your recovery seed secure and offline
2. **Use strong passwords**: Protect wallet files with strong passwords
3. **Backup regularly**: Keep encrypted backups of wallet files
4. **Update software**: Keep Monero GUI and Tari CLI updated

### Network Security

1. **Use TLS for remote connections**: Enable TLS when connecting to remote nodes
2. **Firewall configuration**: Only expose necessary ports
3. **VPN recommended**: Use VPN for additional privacy
4. **Local node preferred**: Run your own node when possible

### API Security

1. **RPC authentication**: Enable authentication for RPC endpoints
2. **Bind to localhost**: Only bind to 127.0.0.1 unless necessary
3. **Rate limiting**: Implement rate limiting for API calls

---

## Next Steps

1. **Test connections**: Verify all wallet connections work
2. **Configure auto-flow**: Set up automatic flow pushing
3. **Monitor balances**: Check wallet balances regularly
4. **Review logs**: Monitor integration logs for issues
5. **Backup wallets**: Ensure you have secure backups

## Support

For issues or questions:
- Monero: https://www.getmonero.org/community/
- Tari: https://www.tari.com/community/
- Dashboard: Check README.md and IMPLEMENTATION.md

---

**Status**: Integration modules ready for use with Monero GUI and Tari CLI wallets
