#!/usr/bin/env python3
"""
Test script for RedCode Quantum Miner Dashboard
Validates all components without launching GUI
"""

import sys
import json
from miner_core import (
    QuantumComputationalEngine,
    RedCodeCoin,
    BitcoinMiner,
    MoneroMiner,
    RedCodeMiner,
    CypherCommunicationLayer,
    MinerDashboardCore
)

def test_quantum_engine():
    """Test quantum computational engine"""
    print("Testing Quantum Computational Engine...")
    engine = QuantumComputationalEngine()
    
    # Test 5D strategy
    import numpy as np
    data = np.random.rand(5)
    result_5d = engine.compute_5d_strategy(data)
    assert result_5d > 0, "5D strategy should return positive value"
    
    # Test 10D tornado convergence
    result_10d = engine.compute_10d_tornado_convergence(100)
    assert result_10d is not None, "10D convergence should return a value"
    
    # Test 100D fractal tree
    result_100d = engine.compute_100d_fractal_tree(5)
    assert result_100d > 0, "100D fractal tree should return positive multiplier"
    
    # Test 1000D waterfall
    result_1000d = engine.compute_1000d_waterfall(1.0)
    assert result_1000d is not None, "1000D waterfall should return a value"
    
    # Verify state
    state = engine.get_computational_state()
    assert '5d' in state and '10d' in state and '100d' in state and '1000d' in state
    
    print("  ✓ All quantum computational tests passed")
    return True

def test_redcode_coin():
    """Test RedCode Coin implementation"""
    print("Testing RedCode Coin (RDC)...")
    coin = RedCodeCoin()
    
    # Verify supply
    assert coin.total_supply == 1_000_000_000, "Total supply should be 1 billion"
    assert coin.symbol == "RDC", "Symbol should be RDC"
    
    # Test wallet creation
    coin.create_wallet("wallet1", 100.0)
    assert coin.get_balance("wallet1") == 100.0, "Wallet balance incorrect"
    
    # Test transfer
    coin.create_wallet("wallet2", 0.0)
    success = coin.transfer("wallet1", "wallet2", 50.0)
    assert success, "Transfer should succeed"
    assert coin.get_balance("wallet1") == 50.0, "Source wallet balance incorrect"
    assert coin.get_balance("wallet2") == 50.0, "Destination wallet balance incorrect"
    
    # Test mining reward
    coin.mint_mining_reward("wallet1", 25.0)
    assert coin.get_balance("wallet1") == 75.0, "Mining reward not applied correctly"
    
    print("  ✓ All RDC coin tests passed")
    return True

def test_miners():
    """Test all three miners"""
    print("Testing Miners...")
    engine = QuantumComputationalEngine()
    coin = RedCodeCoin()
    
    # Test Bitcoin miner
    btc_miner = BitcoinMiner(engine)
    assert btc_miner.name == "Bitcoin", "Bitcoin miner name incorrect"
    assert btc_miner.algorithm == "SHA-256", "Bitcoin algorithm incorrect"
    success, hash_result = btc_miner.mine(difficulty=1)
    assert len(hash_result) == 64, "Hash should be 64 characters"
    
    # Test Monero miner
    xmr_miner = MoneroMiner(engine)
    assert xmr_miner.name == "Monero", "Monero miner name incorrect"
    assert xmr_miner.algorithm == "RandomX", "Monero algorithm incorrect"
    success = xmr_miner.connect_to_wallet("127.0.0.1", 18081)
    assert success, "Monero wallet connection should succeed"
    
    # Test RedCode miner
    rdc_miner = RedCodeMiner(engine, coin)
    assert rdc_miner.name == "RedCode", "RedCode miner name incorrect"
    assert rdc_miner.algorithm == "QuantumProof", "RedCode algorithm incorrect"
    initial_balance = coin.get_balance(rdc_miner.mining_address)
    success, hash_result, reward = rdc_miner.mine_rdc(difficulty=1)
    if success:
        new_balance = coin.get_balance(rdc_miner.mining_address)
        assert new_balance > initial_balance, "RDC reward not minted"
    
    print("  ✓ All miner tests passed")
    return True

def test_cypher_layer():
    """Test AI-to-AI cypher communication"""
    print("Testing Cypher Communication Layer...")
    cypher = CypherCommunicationLayer()
    
    # Test encryption/decryption
    message = "Test quantum communication"
    encrypted = cypher.encrypt_message(message)
    assert encrypted != message, "Message should be encrypted"
    
    decrypted = cypher.decrypt_message(encrypted)
    assert decrypted == message, "Decrypted message should match original"
    
    # Test AI communication
    encrypted_msg = cypher.ai_communicate("AI1", "AI2", "Hello quantum world")
    assert len(cypher.communication_log) > 0, "Communication should be logged"
    
    print("  ✓ All cypher communication tests passed")
    return True

def test_dashboard_core():
    """Test dashboard core integration"""
    print("Testing Dashboard Core...")
    dashboard = MinerDashboardCore()
    
    # Verify initialization
    assert dashboard.quantum_engine is not None, "Quantum engine not initialized"
    assert dashboard.rdc_coin is not None, "RDC coin not initialized"
    assert len(dashboard.miners) == 3, "Should have 3 miners"
    
    # Test mining operations
    dashboard.start_mining()
    assert dashboard.running, "Dashboard should be running"
    
    results = dashboard.mining_cycle(iterations=100)
    assert 'bitcoin' in results and 'monero' in results and 'redcode' in results
    
    dashboard.stop_mining()
    assert not dashboard.running, "Dashboard should be stopped"
    
    # Test state retrieval
    state = dashboard.get_dashboard_state()
    assert 'rdc_coin' in state, "State should include RDC coin info"
    assert 'mining_rates' in state, "State should include mining rates"
    assert 'quantum_state' in state, "State should include quantum state"
    assert 'miners' in state, "State should include miner info"
    
    print("  ✓ All dashboard core tests passed")
    return True

def test_config_file():
    """Test configuration file"""
    print("Testing Configuration File...")
    try:
        import os
        config_path = os.path.join(os.path.dirname(__file__), 'config.json')
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        assert 'redcode_coin' in config, "Config should have RDC info"
        assert 'quantum_dimensions' in config, "Config should have quantum dimensions"
        assert 'miners' in config, "Config should have miner config"
        assert 'monero_wallet' in config, "Config should have Monero wallet config"
        
        # Verify RDC config
        assert config['redcode_coin']['total_supply'] == 1000000000
        
        print("  ✓ Configuration file valid")
        return True
    except Exception as e:
        print(f"  ✗ Configuration test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("RedCode Quantum Miner Dashboard - Test Suite")
    print("=" * 60)
    print()
    
    tests = [
        test_config_file,
        test_quantum_engine,
        test_redcode_coin,
        test_miners,
        test_cypher_layer,
        test_dashboard_core
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"  ✗ Test failed with exception: {e}")
            failed += 1
    
    print()
    print("=" * 60)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("=" * 60)
    
    if failed == 0:
        print("✓ All tests passed successfully!")
        return 0
    else:
        print("✗ Some tests failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())
