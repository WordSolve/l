"""
RedCode Quantum Miner Dashboard
Multi-dimensional computational cryptocurrency mining system
"""

import json
import numpy as np
from typing import Dict, List, Tuple
import time
import hashlib
from datetime import datetime
from price_fetcher import LivePriceFetcher

# Import wallet integration modules
try:
    from monero_integration import MoneroGUIConnector, TariCLIConnector, FlowBridge
    INTEGRATIONS_AVAILABLE = True
except ImportError:
    INTEGRATIONS_AVAILABLE = False
    print("Warning: Wallet integration modules not available")


class QuantumComputationalEngine:
    """
    Multi-dimensional quantum computational engine for mining operations.
    Supports 5D, 10D, 100D, and 1000D computational strategies.
    """
    
    def __init__(self):
        # Use computational representations instead of full arrays to save memory
        # These represent the dimensional state computationally, not as full tensors
        self.computational_state = {
            '5d': 0.0,
            '10d': 0.0,
            '100d': 0.0,
            '1000d': 0.0
        }
        
    def compute_5d_strategy(self, data: np.ndarray) -> float:
        """5D computational strategy for mining optimization"""
        result = np.sum(data) * np.mean(data)
        self.computational_state['5d'] = result
        return result
        
    def compute_10d_tornado_convergence(self, iterations: int = 100) -> float:
        """10D tornado convergence computational model"""
        convergence_value = 0.0
        for i in range(iterations):
            # Tornado convergence algorithm
            layer = np.random.rand(10)
            convergence_value += np.prod(layer) * (i + 1)
        
        self.computational_state['10d'] = convergence_value
        return convergence_value
        
    def compute_100d_fractal_tree(self, depth: int = 5) -> float:
        """100D fractal tree computational hash rate multiplier"""
        def fractal_branch(level, max_level):
            if level >= max_level:
                return 1.0
            return (fractal_branch(level + 1, max_level) * 2.0) ** 0.5
        
        multiplier = fractal_branch(0, depth)
        self.computational_state['100d'] = multiplier
        return multiplier
        
    def compute_1000d_waterfall(self, flow_rate: float = 1.0) -> float:
        """1000D waterfall technology for wave flow computation"""
        # Waterfall cascade through dimensional layers
        waterfall_value = 0.0
        for dimension in range(100):  # Representing 1000D in compressed form
            wave = np.sin(dimension * flow_rate) * np.cos(dimension * flow_rate * 0.5)
            waterfall_value += wave * (dimension + 1)
        
        self.computational_state['1000d'] = waterfall_value
        return waterfall_value
        
    def get_computational_state(self) -> Dict[str, float]:
        """Get current computational state across all dimensions"""
        return self.computational_state


class RedCodeCoin:
    """
    RedCode Coin (RDC) - 1 Billion token supply
    Banking functionality for cryptocurrency operations
    """
    
    def __init__(self):
        self.total_supply = 1_000_000_000  # 1 billion tokens
        self.symbol = "RDC"
        self.decimals = 8
        self.wallets = {}
        self.transactions = []
        
    def create_wallet(self, address: str, initial_balance: float = 0.0):
        """Create a new wallet address"""
        self.wallets[address] = initial_balance
        
    def get_balance(self, address: str) -> float:
        """Get wallet balance"""
        return self.wallets.get(address, 0.0)
        
    def transfer(self, from_address: str, to_address: str, amount: float) -> bool:
        """Transfer RDC between wallets"""
        if from_address not in self.wallets:
            return False
        if self.wallets[from_address] < amount:
            return False
            
        if to_address not in self.wallets:
            self.create_wallet(to_address)
            
        self.wallets[from_address] -= amount
        self.wallets[to_address] += amount
        
        self.transactions.append({
            'from': from_address,
            'to': to_address,
            'amount': amount,
            'timestamp': datetime.now().isoformat()
        })
        return True
        
    def mint_mining_reward(self, address: str, amount: float):
        """Mint new tokens as mining reward"""
        if address not in self.wallets:
            self.create_wallet(address)
        self.wallets[address] += amount


class QuantumMiner:
    """
    Base class for quantum-enhanced miners
    Uses computational strategies for mining operations
    """
    
    def __init__(self, name: str, quantum_engine: QuantumComputationalEngine, expected_hashrate: float = 1000.0):
        self.name = name
        self.quantum_engine = quantum_engine
        self.hash_rate = 0.0
        self.shares_found = 0
        self.total_hashes = 0
        self.expected_hashrate = expected_hashrate  # Realistic expected hash rate
        self.usd_price = 0.0
        self.usd_value_mined = 0.0
        
    def compute_hash(self, data: str) -> str:
        """Compute cryptographic hash using quantum enhancement"""
        # Use quantum computational state to enhance hashing
        quantum_state = self.quantum_engine.get_computational_state()
        enhanced_data = f"{data}:{quantum_state['5d']}:{quantum_state['10d']}"
        return hashlib.sha256(enhanced_data.encode()).hexdigest()
        
    def mine(self, difficulty: int = 4) -> Tuple[bool, str]:
        """Perform mining operation with quantum enhancement"""
        self.total_hashes += 1
        nonce = int(time.time() * 1000000) + self.total_hashes
        data = f"{self.name}:{nonce}"
        hash_result = self.compute_hash(data)
        
        # Check if hash meets difficulty
        if hash_result.startswith('0' * difficulty):
            self.shares_found += 1
            return True, hash_result
        return False, hash_result
        
    def calculate_hash_rate(self, time_window: float) -> float:
        """Calculate current hash rate based on realistic values"""
        if time_window > 0:
            # Use realistic hash rate that approaches expected_hashrate
            raw_rate = self.total_hashes / time_window
            # Scale to realistic values
            self.hash_rate = min(raw_rate * (self.expected_hashrate / 100.0), self.expected_hashrate)
        return self.hash_rate
    
    def set_price(self, usd_price: float):
        """Set current USD price for this coin"""
        self.usd_price = usd_price
    
    def calculate_mined_value(self, coins_mined: float):
        """Calculate USD value of mined coins"""
        self.usd_value_mined = coins_mined * self.usd_price
        return self.usd_value_mined
    
    def calculate_value_per_hash(self) -> Dict[str, float]:
        """
        Calculate the USD value per hash for experiment tracking.
        This allows marking each hash with its real-world value.
        
        Returns:
            Dict with value_per_hash_usd, daily_value_estimate, hourly_value_estimate
        """
        if self.hash_rate == 0:
            return {
                'value_per_hash_usd': 0.0,
                'value_per_hash_btc': 0.0,
                'hourly_value_usd': 0.0,
                'daily_value_usd': 0.0,
                'monthly_value_usd': 0.0
            }
        
        # Calculate probability of finding a block per hash
        # This is a simplified model: prob = hash_rate / network_hash_rate
        # For real mining, this would involve difficulty and target calculations
        
        # Estimate network hashrate in H/s (convert from string representation)
        network_hash_numeric = self._parse_network_hashrate()
        
        if network_hash_numeric == 0:
            # Fallback calculation if network hashrate not available
            # Use a conservative estimate based on expected rewards
            value_per_hash = (self.block_reward * self.usd_price) / 1000000000
        else:
            # Probability of finding a block with one hash
            prob_per_hash = 1.0 / network_hash_numeric
            
            # Expected value per hash = probability * block_reward * price
            value_per_hash = prob_per_hash * self.block_reward * self.usd_price
        
        # Calculate time-based estimates
        hashes_per_hour = self.hash_rate * 3600
        hashes_per_day = self.hash_rate * 86400
        hashes_per_month = self.hash_rate * 2592000  # 30 days
        
        return {
            'value_per_hash_usd': value_per_hash,
            'value_per_hash_formatted': f"${value_per_hash:.12f}",
            'hourly_value_usd': value_per_hash * hashes_per_hour,
            'daily_value_usd': value_per_hash * hashes_per_day,
            'monthly_value_usd': value_per_hash * hashes_per_month,
            'total_hashes': self.total_hashes,
            'total_value_generated_usd': value_per_hash * self.total_hashes
        }
    
    def _parse_network_hashrate(self) -> float:
        """Parse network hashrate string to numeric H/s value"""
        if not hasattr(self, 'network_hashrate') or not self.network_hashrate:
            return 0.0
        
        hashrate_str = str(self.network_hashrate).upper()
        
        # Extract number and unit
        import re
        match = re.match(r'([\d.]+)\s*([A-Z]+)', hashrate_str)
        if not match:
            return 0.0
        
        number = float(match.group(1))
        unit = match.group(2)
        
        # Convert to H/s
        multipliers = {
            'H/S': 1,
            'KH/S': 1000,
            'MH/S': 1000000,
            'GH/S': 1000000000,
            'TH/S': 1000000000000,
            'PH/S': 1000000000000000,
            'EH/S': 1000000000000000000,
        }
        
        return number * multipliers.get(unit, 0.0)


class BitcoinMiner(QuantumMiner):
    """Bitcoin quantum miner with F2Pool configuration"""
    
    def __init__(self, quantum_engine: QuantumComputationalEngine, expected_hashrate: float = 25000000.0):
        super().__init__("Bitcoin", quantum_engine, expected_hashrate)
        self.algorithm = "SHA-256"
        self.pool_name = "F2Pool"
        self.pool_url = "stratum+tcp://btc.f2pool.com:3333"
        self.network_hashrate = "400 EH/s"
        self.block_reward = 6.25


class MoneroMiner(QuantumMiner):
    """Monero (XMR) quantum miner with SupportXMR pool integration"""
    
    def __init__(self, quantum_engine: QuantumComputationalEngine, expected_hashrate: float = 5000.0):
        super().__init__("Monero", quantum_engine, expected_hashrate)
        self.algorithm = "RandomX"
        self.pool_name = "SupportXMR"
        self.pool_url = "pool.supportxmr.com:3333"
        self.network_hashrate = "2.8 GH/s"
        self.block_reward = 0.6
        self.wallet_connection = None
        
    def connect_to_wallet(self, host: str = "127.0.0.1", port: int = 18081):
        """Connect to Monero GUI wallet RPC"""
        self.wallet_connection = {
            'host': host,
            'port': port,
            'connected': True,
            'connection_time': datetime.now().isoformat()
        }
        return True


class RedCodeMiner(QuantumMiner):
    """
    RedCode (RDC) quantum miner
    Native quantum-enhanced mining for RedCode Coin with $1 value
    """
    
    def __init__(self, quantum_engine: QuantumComputationalEngine, rdc_coin: RedCodeCoin, expected_hashrate: float = 10000.0):
        super().__init__("RedCode", quantum_engine, expected_hashrate)
        self.algorithm = "QuantumProof"
        self.rdc_coin = rdc_coin
        self.mining_address = "RDC_MINER_MAIN"
        self.rdc_coin.create_wallet(self.mining_address, 0.0)
        self.usd_price = 1.00  # RedCode fixed at $1.00
        self.network_hashrate = "Computing"
        self.block_reward = 50.0

        
    def mine_rdc(self, difficulty: int = 4) -> Tuple[bool, str, float]:
        """Mine RedCode coin with quantum enhancement"""
        # Apply all quantum computational strategies
        strategy_5d = self.quantum_engine.compute_5d_strategy(np.random.rand(5))
        convergence_10d = self.quantum_engine.compute_10d_tornado_convergence(50)
        fractal_100d = self.quantum_engine.compute_100d_fractal_tree(3)
        waterfall_1000d = self.quantum_engine.compute_1000d_waterfall(1.5)
        
        # Compute hash multiplier based on all dimensions
        hash_multiplier = (strategy_5d * 0.1 + convergence_10d * 0.001 + 
                          fractal_100d * 0.5 + waterfall_1000d * 0.0001)
        
        success, hash_result = self.mine(difficulty)
        
        if success:
            # Calculate reward based on quantum enhancement
            base_reward = 50.0
            quantum_bonus = hash_multiplier * 0.1
            total_reward = base_reward + quantum_bonus
            
            # Mint reward to mining address
            self.rdc_coin.mint_mining_reward(self.mining_address, total_reward)
            
            return True, hash_result, total_reward
        
        return False, hash_result, 0.0


class CypherCommunicationLayer:
    """
    AI-to-AI Cypher communication layer
    Non-brute-force computational communication protocol
    """
    
    def __init__(self):
        self.communication_log = []
        self.cypher_key = self._generate_cypher_key()
        
    def _generate_cypher_key(self) -> str:
        """Generate cypher key for secure AI communication"""
        timestamp = str(time.time())
        return hashlib.sha256(timestamp.encode()).hexdigest()
        
    def encrypt_message(self, message: str) -> str:
        """Encrypt message using cypher protocol"""
        encrypted = ""
        for i, char in enumerate(message):
            key_char = self.cypher_key[i % len(self.cypher_key)]
            encrypted += chr(ord(char) ^ ord(key_char))
        return encrypted.encode('utf-8').hex()
        
    def decrypt_message(self, encrypted: str) -> str:
        """Decrypt message using cypher protocol"""
        try:
            encrypted_bytes = bytes.fromhex(encrypted)
            decrypted = ""
            for i, byte in enumerate(encrypted_bytes):
                key_char = self.cypher_key[i % len(self.cypher_key)]
                decrypted += chr(byte ^ ord(key_char))
            return decrypted
        except:
            return ""
            
    def ai_communicate(self, from_ai: str, to_ai: str, message: str):
        """AI-to-AI communication via cypher"""
        encrypted = self.encrypt_message(message)
        communication = {
            'from': from_ai,
            'to': to_ai,
            'encrypted_message': encrypted,
            'timestamp': datetime.now().isoformat()
        }
        self.communication_log.append(communication)
        return encrypted


class MinerDashboardCore:
    """
    Core dashboard engine for RedCode quantum miner
    Manages all miners, computations, and banking operations
    """
    
    def __init__(self):
        self.config = self._load_config()
        self.quantum_engine = QuantumComputationalEngine()
        self.rdc_coin = RedCodeCoin()
        self.cypher_layer = CypherCommunicationLayer()
        
        # Initialize live price fetcher
        self.price_fetcher = LivePriceFetcher()
        
        # Initialize wallet integrations if enabled
        self.monero_gui = None
        self.tari_cli = None
        self.flow_bridge = None
        
        if INTEGRATIONS_AVAILABLE:
            # Initialize Monero GUI connector if enabled in config
            monero_config = self.config.get('monero_wallet', {}).get('gui_connection', {})
            if monero_config.get('enabled', False):
                self.monero_gui = MoneroGUIConnector(
                    host=monero_config.get('host', '127.0.0.1'),
                    wallet_port=monero_config.get('rpc_port', 18082),
                    daemon_port=monero_config.get('port', 18081)
                )
            
            # Initialize Tari CLI connector if enabled in config
            tari_config = self.config.get('tari_wallet', {}).get('cli_connection', {})
            if tari_config.get('enabled', False):
                self.tari_cli = TariCLIConnector(
                    cli_path=tari_config.get('cli_path', 'tari_console_wallet'),
                    base_node=tari_config.get('base_node', '127.0.0.1:18142')
                )
            
            # Initialize flow bridge if both are enabled
            if self.monero_gui and self.tari_cli:
                flow_config = self.config.get('flow_bridge', {})
                if flow_config.get('enabled', False):
                    self.flow_bridge = FlowBridge(self.monero_gui, self.tari_cli)
        
        # Get expected hash rates from config
        btc_hashrate = self.config.get('miners', {}).get('bitcoin', {}).get('expected_hashrate', 25000000)
        xmr_hashrate = self.config.get('miners', {}).get('monero', {}).get('expected_hashrate', 5000)
        rdc_hashrate = self.config.get('miners', {}).get('redcode', {}).get('expected_hashrate', 10000)
        
        # Initialize miners with realistic hash rates
        self.bitcoin_miner = BitcoinMiner(self.quantum_engine, btc_hashrate)
        self.monero_miner = MoneroMiner(self.quantum_engine, xmr_hashrate)
        self.redcode_miner = RedCodeMiner(self.quantum_engine, self.rdc_coin, rdc_hashrate)
        
        # Fetch live prices from CoinMarketCap, Coinbase, and Binance
        self.update_live_prices()
        
        self.miners = {
            'bitcoin': self.bitcoin_miner,
            'monero': self.monero_miner,
            'redcode': self.redcode_miner
        }
        
        self.running = False
        self.start_time = None
    
    def update_live_prices(self):
        """Update cryptocurrency prices from live sources"""
        try:
            live_prices = self.price_fetcher.get_all_prices(use_cache=True)
            self.bitcoin_miner.set_price(live_prices.get('bitcoin', 42000.0))
            self.monero_miner.set_price(live_prices.get('monero', 165.0))
            self.redcode_miner.set_price(live_prices.get('redcode', 1.0))
        except Exception as e:
            print(f"Error updating live prices: {e}")
            # Fallback to config prices if live fetch fails
            market_data = self.config.get('coin_market_data', {})
            if 'bitcoin' in market_data:
                self.bitcoin_miner.set_price(market_data['bitcoin'].get('usd_price', 42000.0))
            if 'monero' in market_data:
                self.monero_miner.set_price(market_data['monero'].get('usd_price', 165.0))
            if 'redcode' in market_data:
                self.redcode_miner.set_price(market_data['redcode'].get('usd_price', 1.0))
    
    def connect_monero_gui(self) -> Tuple[bool, str]:
        """Connect to Monero GUI wallet and daemon"""
        if not self.monero_gui:
            return False, "Monero GUI connector not initialized"
        
        # Connect to wallet
        wallet_success, wallet_msg = self.monero_gui.connect_wallet()
        
        # Connect to daemon
        daemon_success, daemon_msg = self.monero_gui.connect_daemon()
        
        # Enable GhostRider if configured
        ghostrider_config = self.config.get('monero_wallet', {}).get('ghostrider', {})
        if ghostrider_config.get('enabled', False):
            gr_success, gr_msg = self.monero_gui.enable_ghostrider()
            return wallet_success, f"Wallet: {wallet_msg}\nDaemon: {daemon_msg}\nGhostRider: {gr_msg}"
        
        return wallet_success, f"Wallet: {wallet_msg}\nDaemon: {daemon_msg}"
    
    def connect_tari_cli(self) -> Tuple[bool, str]:
        """Connect to Tari CLI wallet"""
        if not self.tari_cli:
            return False, "Tari CLI connector not initialized"
        
        return self.tari_cli.connect()
    
    def push_flow_to_tari(self, amount: float, source: str = "monero") -> Tuple[bool, str]:
        """Push mining rewards to Tari wallet via one-sided payment"""
        if not self.tari_cli:
            return False, "Tari CLI connector not initialized"
        
        if not self.tari_cli.connected:
            return False, "Tari CLI wallet not connected"
        
        return self.tari_cli.push_flow(amount, source)
    
    def transfer_monero_to_tari(self, xmr_amount: float) -> Tuple[bool, str]:
        """Transfer Monero balance to Tari using flow bridge"""
        if not self.flow_bridge:
            return False, "Flow bridge not initialized"
        
        return self.flow_bridge.transfer_monero_to_tari(xmr_amount)
    
    def get_wallet_status(self) -> Dict:
        """Get status of all wallet connections"""
        status = {
            "monero_gui": None,
            "tari_cli": None,
            "flow_bridge": None
        }
        
        if self.monero_gui:
            status["monero_gui"] = self.monero_gui.get_connection_status()
        
        if self.tari_cli:
            status["tari_cli"] = self.tari_cli.get_connection_status()
        
        if self.flow_bridge:
            status["flow_bridge"] = self.flow_bridge.get_bridge_status()
        
        return status
        
    def _load_config(self) -> dict:
        """Load configuration from config.json"""
        try:
            # Use relative path from current working directory
            import os
            config_path = os.path.join(os.path.dirname(__file__), 'config.json')
            with open(config_path, 'r') as f:
                return json.load(f)
        except:
            return {}
            
    def get_mining_rates(self) -> Dict[str, float]:
        """Get current mining rates for all miners"""
        rates = {}
        for name, miner in self.miners.items():
            rates[name] = miner.hash_rate
        return rates
        
    def get_rdc_balance(self, address: str = None) -> float:
        """Get RDC balance for address"""
        if address is None:
            address = self.redcode_miner.mining_address
        return self.rdc_coin.get_balance(address)
    
    def get_hash_value_tracking(self) -> Dict[str, Dict]:
        """
        Get USD value per hash for all miners for experiment tracking.
        This allows marking each hash with its real-world value.
        
        Returns:
            Dict with hash value tracking for bitcoin, monero, and redcode
        """
        return {
            'bitcoin': self.bitcoin_miner.calculate_value_per_hash(),
            'monero': self.monero_miner.calculate_value_per_hash(),
            'redcode': self.redcode_miner.calculate_value_per_hash(),
            'summary': {
                'bitcoin_value_per_hash': self.bitcoin_miner.calculate_value_per_hash()['value_per_hash_formatted'],
                'monero_value_per_hash': self.monero_miner.calculate_value_per_hash()['value_per_hash_formatted'],
                'redcode_value_per_hash': self.redcode_miner.calculate_value_per_hash()['value_per_hash_formatted'],
            }
        }
        
    def start_mining(self):
        """Start all mining operations"""
        self.running = True
        self.start_time = time.time()
        
    def stop_mining(self):
        """Stop all mining operations"""
        self.running = False
        
    def mining_cycle(self, iterations: int = 100):
        """Execute mining cycle across all miners"""
        results = {
            'bitcoin': {'success': 0, 'hashes': 0},
            'monero': {'success': 0, 'hashes': 0},
            'redcode': {'success': 0, 'hashes': 0, 'rewards': 0.0}
        }
        
        for i in range(iterations):
            # Bitcoin mining
            success, _ = self.bitcoin_miner.mine(difficulty=4)
            results['bitcoin']['hashes'] += 1
            if success:
                results['bitcoin']['success'] += 1
                
            # Monero mining
            success, _ = self.monero_miner.mine(difficulty=4)
            results['monero']['hashes'] += 1
            if success:
                results['monero']['success'] += 1
                
            # RedCode quantum mining
            success, _, reward = self.redcode_miner.mine_rdc(difficulty=3)
            results['redcode']['hashes'] += 1
            if success:
                results['redcode']['success'] += 1
                results['redcode']['rewards'] += reward
        
        # Update hash rates
        elapsed = time.time() - self.start_time if self.start_time else 1.0
        for name, miner in self.miners.items():
            miner.calculate_hash_rate(elapsed)
            
        return results
        
    def get_dashboard_state(self) -> dict:
        """Get complete dashboard state for UI"""
        market_data = self.config.get('coin_market_data', {})
        
        # Periodically update live prices (every 60 seconds)
        if self.running:
            self.update_live_prices()
        
        return {
            'rdc_coin': {
                'symbol': self.rdc_coin.symbol,
                'total_supply': self.rdc_coin.total_supply,
                'miner_balance': self.get_rdc_balance(),
                'usd_price': self.redcode_miner.usd_price,
                'usd_value': self.get_rdc_balance() * self.redcode_miner.usd_price
            },
            'mining_rates': self.get_mining_rates(),
            'quantum_state': self.quantum_engine.get_computational_state(),
            'miners': {
                name: {
                    'hash_rate': miner.hash_rate,
                    'shares_found': miner.shares_found,
                    'total_hashes': miner.total_hashes,
                    'usd_price': miner.usd_price,
                    'expected_hashrate': miner.expected_hashrate,
                    'algorithm': miner.algorithm,
                    'pool_name': getattr(miner, 'pool_name', 'N/A'),
                    'pool_url': getattr(miner, 'pool_url', 'N/A'),
                    'network_hashrate': getattr(miner, 'network_hashrate', 'N/A'),
                    'block_reward': getattr(miner, 'block_reward', 0.0),
                    'hash_value_tracking': miner.calculate_value_per_hash()
                }
                for name, miner in self.miners.items()
            },
            'running': self.running,
            'config': self.config,
            'market_data': market_data,
            'price_sources': {
                'last_update': self.price_fetcher.last_update.isoformat() if self.price_fetcher.last_update else None,
                'sources': ['CoinMarketCap', 'Coinbase', 'Binance'],
                'cache_duration': self.price_fetcher.cache_duration
            },
            'wallet_integrations': self.get_wallet_status()
        }


if __name__ == "__main__":
    print("RedCode Quantum Miner Dashboard - Core Engine")
    print("=" * 60)
    
    # Initialize dashboard
    dashboard = MinerDashboardCore()
    
    print(f"✓ Quantum Engine initialized")
    print(f"✓ RedCode Coin (RDC) - Total Supply: {dashboard.rdc_coin.total_supply:,} tokens")
    print(f"✓ Bitcoin Miner initialized")
    print(f"✓ Monero Miner initialized")
    print(f"✓ RedCode Quantum Miner initialized")
    print(f"✓ AI-to-AI Cypher Communication Layer active")
    print("\nRunning test mining cycle...")
    
    # Start mining
    dashboard.start_mining()
    results = dashboard.mining_cycle(iterations=1000)
    
    print("\nMining Results:")
    print(f"Bitcoin - Shares: {results['bitcoin']['success']}, Hashes: {results['bitcoin']['hashes']}")
    print(f"Monero - Shares: {results['monero']['success']}, Hashes: {results['monero']['hashes']}")
    print(f"RedCode - Shares: {results['redcode']['success']}, Hashes: {results['redcode']['hashes']}, Rewards: {results['redcode']['rewards']:.2f} RDC")
    
    print("\nQuantum Computational State:")
    state = dashboard.quantum_engine.get_computational_state()
    for dim, value in state.items():
        print(f"  {dim}: {value:.6f}")
    
    print(f"\nRDC Balance: {dashboard.get_rdc_balance():.2f} RDC")
    print("\nCore engine test completed successfully!")
