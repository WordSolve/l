"""
Test script to demonstrate hash value tracking feature
"""

from miner_core import MinerDashboardCore

def main():
    print("=" * 70)
    print("RedCode Quantum Miner Dashboard - Hash Value Tracking Demo")
    print("=" * 70)
    print()
    
    # Initialize dashboard
    dashboard = MinerDashboardCore()
    
    # Start mining
    print("Starting mining operations...")
    dashboard.start_mining()
    
    # Run some mining cycles to generate hashes
    print("Mining 10,000 iterations...")
    results = dashboard.mining_cycle(iterations=10000)
    print(f"✓ Mining completed")
    print()
    
    # Get hash value tracking
    print("=" * 70)
    print("HASH VALUE TRACKING - Experiment Marking Data")
    print("=" * 70)
    print()
    
    hash_tracking = dashboard.get_hash_value_tracking()
    
    # Bitcoin tracking
    print("🔶 BITCOIN (BTC) - F2Pool")
    print("-" * 70)
    btc = hash_tracking['bitcoin']
    print(f"  Value Per Hash:        {btc['value_per_hash_formatted']}")
    print(f"  Total Hashes Computed: {btc['total_hashes']:,}")
    print(f"  Total Value Generated: ${btc['total_value_generated_usd']:.12f} USD")
    print(f"  Hourly Value Estimate: ${btc['hourly_value_usd']:.6f} USD")
    print(f"  Daily Value Estimate:  ${btc['daily_value_usd']:.4f} USD")
    print(f"  Monthly Value Est:     ${btc['monthly_value_usd']:.2f} USD")
    print()
    
    # Monero tracking
    print("🟠 MONERO (XMR) - SupportXMR")
    print("-" * 70)
    xmr = hash_tracking['monero']
    print(f"  Value Per Hash:        {xmr['value_per_hash_formatted']}")
    print(f"  Total Hashes Computed: {xmr['total_hashes']:,}")
    print(f"  Total Value Generated: ${xmr['total_value_generated_usd']:.12f} USD")
    print(f"  Hourly Value Estimate: ${xmr['hourly_value_usd']:.6f} USD")
    print(f"  Daily Value Estimate:  ${xmr['daily_value_usd']:.4f} USD")
    print(f"  Monthly Value Est:     ${xmr['monthly_value_usd']:.2f} USD")
    print()
    
    # RedCode tracking
    print("🟢 REDCODE (RDC) - $1.00 Fixed Value")
    print("-" * 70)
    rdc = hash_tracking['redcode']
    print(f"  Value Per Hash:        {rdc['value_per_hash_formatted']}")
    print(f"  Total Hashes Computed: {rdc['total_hashes']:,}")
    print(f"  Total Value Generated: ${rdc['total_value_generated_usd']:.12f} USD")
    print(f"  Hourly Value Estimate: ${rdc['hourly_value_usd']:.6f} USD")
    print(f"  Daily Value Estimate:  ${rdc['daily_value_usd']:.4f} USD")
    print(f"  Monthly Value Est:     ${rdc['monthly_value_usd']:.2f} USD")
    print()
    
    print("=" * 70)
    print("SUMMARY - Quick Reference for Experiment Marking")
    print("=" * 70)
    summary = hash_tracking['summary']
    print(f"  BTC Value/Hash: {summary['bitcoin_value_per_hash']}")
    print(f"  XMR Value/Hash: {summary['monero_value_per_hash']}")
    print(f"  RDC Value/Hash: {summary['redcode_value_per_hash']}")
    print()
    
    print("=" * 70)
    print("How to Use This Data in Your Experiment:")
    print("=" * 70)
    print("  1. Each hash you compute has a specific USD value")
    print("  2. Use 'Value Per Hash' to mark each hash in your records")
    print("  3. Track 'Total Value Generated' to see cumulative value")
    print("  4. Compare efficiency across different coins using value/hash")
    print("  5. Daily/Monthly estimates help with long-term experiment planning")
    print()
    print("✓ Hash value tracking demonstration complete!")
    print()

if __name__ == "__main__":
    main()
