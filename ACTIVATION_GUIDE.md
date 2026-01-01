# Experimental Features Activation Guide

## Overview

The RedCode Quantum Miner Dashboard is designed for research and experimentation. By default, ALL experimental features are **NOT ACTIVATED** to ensure safe testing. This guide shows you exactly what to enable for your experiments.

## Current Status: ALL FEATURES DISABLED

The dashboard runs in **SIMULATION MODE** by default. You can see what's not activated in the UI, and this guide shows you how to turn features on for your experiments.

## How to Activate Features

Edit the `config.json` file and change the appropriate flags from `false` to `true`.

---

## 🔬 Experimental Features Configuration

### 1. Real Mining Mode

**Current Status:** `NOT ACTIVATED`

**What it does:** Switches from simulation to actual mining operations

**How to activate:**
```json
"experiment_features": {
  "real_mining_mode": true
}
```

**When activated:**
- Dashboard will attempt to connect to real mining pools
- You must configure pool URLs and wallet addresses
- Simulation mode will be disabled

---

### 2. Quantum 5D Strategy

**Current Status:** `NOT ACTIVATED`

**What it does:** Enables 5-dimensional computational mining optimization

**How to activate:**
```json
"experiment_features": {
  "quantum_5d_strategy": true
}
```

**When activated:**
- Computes: `result = sum(data) * mean(data)`
- Enhances hash computations with 5D optimization
- UI will show actual 5D values instead of "NOT ACTIVATED"

---

### 3. Quantum 10D Tornado Convergence

**Current Status:** `NOT ACTIVATED`

**What it does:** Enables tornado convergence algorithms across 10 dimensions

**How to activate:**
```json
"experiment_features": {
  "quantum_10d_tornado": true
}
```

**When activated:**
- Iterative layer multiplication patterns
- Convergence value calculations
- UI displays live 10D tornado convergence values

---

### 4. Quantum 100D Fractal Tree

**Current Status:** `NOT ACTIVATED`

**What it does:** Enables 100-dimensional fractal tree hash rate multiplier

**How to activate:**
```json
"experiment_features": {
  "quantum_100d_fractal": true
}
```

**When activated:**
- Recursive fractal branching algorithm
- Hash rate multiplication based on fractal depth
- UI shows 100D fractal multiplier values

---

### 5. Quantum 1000D Waterfall Technology

**Current Status:** `NOT ACTIVATED`

**What it does:** Enables wave flow cascade across 1000 dimensions

**How to activate:**
```json
"experiment_features": {
  "quantum_1000d_waterfall": true
}
```

**When activated:**
- Sin/cos wave cascade computations
- 1000-dimensional waterfall flow processing
- UI displays 1000D waterfall values

---

### 6. Bitcoin Real Network Mining

**Current Status:** `NOT ACTIVATED`

**What it does:** Connects Bitcoin miner to actual Bitcoin network/pool

**How to activate:**
```json
"experiment_features": {
  "bitcoin_real_network": true
},
"miners": {
  "bitcoin": {
    "enabled": true,
    "simulated": false,
    "real_pool_url": "stratum+tcp://your-pool-url:port",
    "real_wallet_address": "your-bitcoin-address"
  }
}
```

**When activated:**
- Bitcoin miner shows "REAL MINING" mode
- Real Mining Rate displays as "ACTIVATED"
- Connects to specified pool
- **WARNING:** Requires valid pool credentials

---

### 7. Monero Real Network Mining

**Current Status:** `NOT ACTIVATED`

**What it does:** Connects Monero miner to actual Monero network/pool

**How to activate:**
```json
"experiment_features": {
  "monero_real_network": true
},
"miners": {
  "monero": {
    "enabled": true,
    "simulated": false,
    "real_pool_url": "your-monero-pool-url:port",
    "real_wallet_address": "your-monero-address"
  }
}
```

**When activated:**
- Monero miner shows "REAL MINING" mode
- Real Mining Rate displays as "ACTIVATED"
- Connects to Monero GUI wallet RPC
- **WARNING:** Requires Monero wallet connection

---

### 8. RedCode Quantum Boost

**Current Status:** `NOT ACTIVATED`

**What it does:** Enables quantum bonus rewards for RedCode mining

**How to activate:**
```json
"experiment_features": {
  "redcode_quantum_boost": true
},
"miners": {
  "redcode": {
    "enabled": true,
    "simulated": false,
    "quantum_boost_active": true
  }
}
```

**When activated:**
- RedCode miner applies quantum multiplier to rewards
- Base reward: 50 RDC
- Quantum bonus: Based on all active quantum dimensions
- UI shows "Quantum Boost: ACTIVATED"

---

## 📋 Quick Activation Examples

### Example 1: Enable All Quantum Features (Simulation Mode)

Perfect for testing quantum algorithms without real mining:

```json
{
  "experiment_features": {
    "real_mining_mode": false,
    "quantum_5d_strategy": true,
    "quantum_10d_tornado": true,
    "quantum_100d_fractal": true,
    "quantum_1000d_waterfall": true,
    "bitcoin_real_network": false,
    "monero_real_network": false,
    "redcode_quantum_boost": true
  }
}
```

**Result:** All quantum computations run, but no real network mining.

---

### Example 2: Enable Bitcoin Real Mining Only

Test Bitcoin mining without quantum features:

```json
{
  "experiment_features": {
    "real_mining_mode": true,
    "quantum_5d_strategy": false,
    "quantum_10d_tornado": false,
    "quantum_100d_fractal": false,
    "quantum_1000d_waterfall": false,
    "bitcoin_real_network": true,
    "monero_real_network": false,
    "redcode_quantum_boost": false
  },
  "miners": {
    "bitcoin": {
      "enabled": true,
      "simulated": false,
      "real_pool_url": "stratum+tcp://pool.example.com:3333",
      "real_wallet_address": "your-btc-address"
    }
  }
}
```

**Result:** Bitcoin mines on real network, everything else in simulation.

---

### Example 3: Full Quantum + RedCode Boost (No Real Networks)

Maximum quantum experimentation in safe simulation:

```json
{
  "experiment_features": {
    "real_mining_mode": false,
    "quantum_5d_strategy": true,
    "quantum_10d_tornado": true,
    "quantum_100d_fractal": true,
    "quantum_1000d_waterfall": true,
    "bitcoin_real_network": false,
    "monero_real_network": false,
    "redcode_quantum_boost": true
  },
  "miners": {
    "redcode": {
      "enabled": true,
      "simulated": true,
      "quantum_boost_active": true
    }
  }
}
```

**Result:** Full quantum stack active, maximum computational research, no real mining.

---

## 🎯 What You'll See in the UI

### When Features Are NOT Activated (Default)

**Mining Statistics:**
- Bitcoin (BTC) - SIMULATED
  - Mode: SIMULATION
  - Real Mining Rate: **NOT ACTIVATED** (red)
  
- Monero (XMR) - SIMULATED
  - Mode: SIMULATION
  - Real Mining Rate: **NOT ACTIVATED** (red)
  
- RedCode (RDC) - SIMULATED
  - Mode: SIMULATION
  - Real Mining Rate: **NOT ACTIVATED** (red)
  - Quantum Boost: **NOT ACTIVATED** (red)

**Quantum Experimental Features:**
- ⚠️ EXPERIMENTAL FEATURES (NOT ACTIVATED):
  - 5D Strategy: **NOT ACTIVATED** (red)
  - 10D Tornado Conv: **NOT ACTIVATED** (red)
  - 100D Fractal Tree: **NOT ACTIVATED** (red)
  - 1000D Waterfall: **NOT ACTIVATED** (red)

**Real Mining Mode:**
- 💡 Set real_mining_mode=true in config.json to activate

---

### When Features ARE Activated

**Example with quantum features enabled:**

**Quantum Experimental Features:**
- 5D Strategy: **ACTIVE: 1.692732** (green)
  → Quantum 5D Strategy is ENABLED
- 10D Tornado Conv: **ACTIVE: 1.753406** (green)
  → Quantum 10D Tornado is ENABLED
- 100D Fractal Tree: **ACTIVE: 1.834008** (green)
  → Quantum 100D Fractal is ENABLED
- 1000D Waterfall: **ACTIVE: -30.033078** (green)
  → Quantum 1000D Waterfall is ENABLED

---

## ⚠️ Important Safety Notes

### Before Activating Real Mining:

1. **Test in Simulation First**
   - Always test with `real_mining_mode: false` first
   - Verify quantum computations work as expected
   - Check hash rates and CPU usage

2. **Real Mining Requirements**
   - Valid pool URLs for Bitcoin/Monero
   - Valid wallet addresses
   - Monero GUI wallet running (for XMR)
   - Adequate CPU/GPU resources

3. **CPU Usage Warning**
   - Quantum features increase CPU usage
   - Start with one quantum feature at a time
   - Monitor system resources

4. **Network Mining Risks**
   - Real mining may incur costs
   - Ensure correct pool configurations
   - Verify wallet addresses before starting
   - This is experimental software - use at your own risk

---

## 🧪 Recommended Testing Sequence

### Phase 1: Baseline (Everything Disabled)
```json
All experiment_features: false
```
- Verify dashboard runs
- Check simulation mode works
- Baseline CPU usage

### Phase 2: Single Quantum Feature
```json
"quantum_5d_strategy": true  (only this one)
```
- Test 5D computations
- Measure CPU impact
- Verify UI updates correctly

### Phase 3: Add More Quantum Features
```json
"quantum_5d_strategy": true,
"quantum_10d_tornado": true
```
- Test multiple quantum dimensions
- Measure combined CPU impact

### Phase 4: Full Quantum Stack
```json
All quantum features: true
```
- Maximum computational load test
- Verify all quantum algorithms work together

### Phase 5: Real Mining (Optional)
```json
"real_mining_mode": true,
"bitcoin_real_network": true  (or monero)
```
- Only after thorough simulation testing
- With valid pool/wallet configuration
- Monitor carefully

---

## 📊 Monitoring Your Experiments

### What to Watch:

1. **Hash Rates**
   - Displayed in real-time for each miner
   - Should increase when quantum features are active

2. **Quantum Values**
   - 5D, 10D, 100D, 1000D computational states
   - Change in real-time when features are active
   - Green = active, Red = not activated

3. **CPU Usage**
   - Use system monitor
   - More quantum features = higher CPU usage
   - Adjust iterations if needed

4. **RDC Balance**
   - Increases when mining finds shares
   - Quantum boost increases rewards when active

---

## 🔧 Troubleshooting

### Feature Not Activating?

1. Check `config.json` syntax is valid JSON
2. Ensure flag is `true` not `"true"` (no quotes on boolean)
3. Restart the dashboard after changing config
4. Check console for error messages

### UI Still Shows "NOT ACTIVATED"?

1. Verify the config file was saved
2. Check file location is correct
3. Restart the application
4. Check config is being loaded (see console output)

### Real Mining Not Working?

1. Ensure `real_mining_mode: true`
2. Verify pool URL format is correct
3. Check wallet address is valid
4. For Monero: ensure GUI wallet is running
5. Check network connectivity

---

## 📝 Configuration File Reference

Complete `config.json` with all flags:

```json
{
  "redcode_coin": {
    "name": "RedCode Coin",
    "symbol": "RDC",
    "total_supply": 1000000000,
    "decimals": 8
  },
  "experiment_features": {
    "real_mining_mode": false,
    "quantum_5d_strategy": false,
    "quantum_10d_tornado": false,
    "quantum_100d_fractal": false,
    "quantum_1000d_waterfall": false,
    "bitcoin_real_network": false,
    "monero_real_network": false,
    "redcode_quantum_boost": false
  },
  "miners": {
    "bitcoin": {
      "enabled": true,
      "simulated": true,
      "real_pool_url": "",
      "real_wallet_address": ""
    },
    "monero": {
      "enabled": true,
      "simulated": true,
      "real_pool_url": "",
      "real_wallet_address": ""
    },
    "redcode": {
      "enabled": true,
      "simulated": true,
      "quantum_boost_active": false
    }
  },
  "fractal_tree": {
    "dimensions": 100,
    "hash_multiplier": 1.0,
    "activated": false
  },
  "waterfall_technology": {
    "dimensions": 1000,
    "flow_rate": 1.0,
    "activated": false
  },
  "monero_wallet": {
    "gui_connection": {
      "host": "127.0.0.1",
      "port": 18081,
      "rpc_port": 18082,
      "connected": false
    }
  }
}
```

---

## 🎓 Summary

- **Default State:** Everything is NOT ACTIVATED (safe simulation mode)
- **Visibility:** UI clearly shows what's not activated in RED
- **Activation:** Edit config.json and change flags from `false` to `true`
- **Verification:** UI turns features GREEN when activated
- **Experimentation:** Enable features one at a time to test
- **Safety:** Test in simulation before attempting real mining

**The dashboard is designed to show you exactly what needs to be turned on for your experiments!**
