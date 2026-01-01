"""
RedCode Quantum Miner Dashboard - Python UI
Full-featured mining dashboard with real-time visualization
"""

import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
from datetime import datetime
from miner_core import MinerDashboardCore
import json


class MinerDashboardUI:
    """
    Python Tkinter UI for RedCode Quantum Miner Dashboard
    Features: Real-time rates, RDC banking, multi-dimensional computational display
    """
    
    def __init__(self, root):
        self.root = root
        self.root.title("RedCode Quantum Miner Dashboard")
        self.root.geometry("1200x800")
        self.root.configure(bg='#0d1117')
        
        # Initialize core
        self.core = MinerDashboardCore()
        self.mining_thread = None
        self.update_thread = None
        self.running = False
        
        # Setup UI
        self.setup_ui()
        
        # Start update loop
        self.start_update_loop()
        
    def setup_ui(self):
        """Setup the complete UI layout"""
        # Title Frame
        title_frame = tk.Frame(self.root, bg='#161b22', height=80)
        title_frame.pack(fill=tk.X, padx=10, pady=10)
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(
            title_frame, 
            text="⚡ RedCode Quantum Miner Dashboard ⚡",
            font=('Arial', 24, 'bold'),
            fg='#58a6ff',
            bg='#161b22'
        )
        title_label.pack(pady=20)
        
        # Main container
        main_container = tk.Frame(self.root, bg='#0d1117')
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Left panel - Mining Stats
        left_panel = tk.Frame(main_container, bg='#161b22', width=400)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        self.setup_mining_stats_panel(left_panel)
        
        # Right panel - RDC Bank & Quantum State
        right_panel = tk.Frame(main_container, bg='#161b22', width=400)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
        
        self.setup_rdc_panel(right_panel)
        self.setup_quantum_panel(right_panel)
        
        # Bottom panel - Controls
        bottom_panel = tk.Frame(self.root, bg='#161b22', height=100)
        bottom_panel.pack(fill=tk.X, padx=10, pady=10)
        bottom_panel.pack_propagate(False)
        
        self.setup_control_panel(bottom_panel)
        
    def setup_mining_stats_panel(self, parent):
        """Setup mining statistics panel"""
        label = tk.Label(
            parent,
            text="⛏️ Mining Statistics",
            font=('Arial', 16, 'bold'),
            fg='#58a6ff',
            bg='#161b22'
        )
        label.pack(pady=10)
        
        # Bitcoin Miner
        self.btc_frame = self.create_miner_frame(parent, "Bitcoin (BTC) - F2Pool", "#f7931a")
        self.btc_price = self.create_stat_label(self.btc_frame, "Price:", "$0.00")
        self.btc_mode = self.create_stat_label(self.btc_frame, "Mode:", "SIMULATION")
        self.btc_hashrate = self.create_stat_label(self.btc_frame, "Hash Rate:", "0 H/s")
        self.btc_expected = self.create_stat_label(self.btc_frame, "Expected Rate:", "0 H/s")
        self.btc_pool = self.create_stat_label(self.btc_frame, "Pool:", "F2Pool")
        self.btc_real_rate = self.create_stat_label(self.btc_frame, "Real Mining Rate:", "NOT ACTIVATED")
        self.btc_shares = self.create_stat_label(self.btc_frame, "Shares:", "0")
        self.btc_hashes = self.create_stat_label(self.btc_frame, "Total Hashes:", "0")
        
        # Monero Miner
        self.xmr_frame = self.create_miner_frame(parent, "Monero (XMR) - SupportXMR", "#ff6600")
        self.xmr_price = self.create_stat_label(self.xmr_frame, "Price:", "$0.00")
        self.xmr_mode = self.create_stat_label(self.xmr_frame, "Mode:", "SIMULATION")
        self.xmr_hashrate = self.create_stat_label(self.xmr_frame, "Hash Rate:", "0 H/s")
        self.xmr_expected = self.create_stat_label(self.xmr_frame, "Expected Rate:", "0 H/s")
        self.xmr_pool = self.create_stat_label(self.xmr_frame, "Pool:", "SupportXMR")
        self.xmr_real_rate = self.create_stat_label(self.xmr_frame, "Real Mining Rate:", "NOT ACTIVATED")
        self.xmr_shares = self.create_stat_label(self.xmr_frame, "Shares:", "0")
        self.xmr_hashes = self.create_stat_label(self.xmr_frame, "Total Hashes:", "0")
        
        # RedCode Miner
        self.rdc_miner_frame = self.create_miner_frame(parent, "RedCode (RDC) - $1.00", "#00ff88")
        self.rdc_price = self.create_stat_label(self.rdc_miner_frame, "Price:", "$1.00")
        self.rdc_mode = self.create_stat_label(self.rdc_miner_frame, "Mode:", "SIMULATION")
        self.rdc_hashrate = self.create_stat_label(self.rdc_miner_frame, "Hash Rate:", "0 H/s")
        self.rdc_expected = self.create_stat_label(self.rdc_miner_frame, "Expected Rate:", "0 H/s")
        self.rdc_value = self.create_stat_label(self.rdc_miner_frame, "Mined Value:", "$0.00")
        self.rdc_real_rate = self.create_stat_label(self.rdc_miner_frame, "Real Mining Rate:", "NOT ACTIVATED")
        self.rdc_quantum_boost = self.create_stat_label(self.rdc_miner_frame, "Quantum Boost:", "NOT ACTIVATED")
        self.rdc_shares = self.create_stat_label(self.rdc_miner_frame, "Shares:", "0")
        self.rdc_hashes = self.create_stat_label(self.rdc_miner_frame, "Total Hashes:", "0")
        
    def create_miner_frame(self, parent, title, color):
        """Create a frame for individual miner stats"""
        frame = tk.LabelFrame(
            parent,
            text=title,
            font=('Arial', 12, 'bold'),
            fg=color,
            bg='#0d1117',
            relief=tk.RIDGE,
            bd=2
        )
        frame.pack(fill=tk.X, padx=10, pady=5)
        return frame
        
    def create_stat_label(self, parent, label_text, value_text):
        """Create a stat label pair"""
        container = tk.Frame(parent, bg='#0d1117')
        container.pack(fill=tk.X, padx=5, pady=2)
        
        label = tk.Label(
            container,
            text=label_text,
            font=('Arial', 10),
            fg='#8b949e',
            bg='#0d1117',
            anchor='w'
        )
        label.pack(side=tk.LEFT)
        
        value = tk.Label(
            container,
            text=value_text,
            font=('Arial', 10, 'bold'),
            fg='#ffffff',
            bg='#0d1117',
            anchor='e'
        )
        value.pack(side=tk.RIGHT)
        
        return value
        
    def setup_rdc_panel(self, parent):
        """Setup RDC Bank panel"""
        label = tk.Label(
            parent,
            text="🏦 RDC Bank",
            font=('Arial', 16, 'bold'),
            fg='#00ff88',
            bg='#161b22'
        )
        label.pack(pady=10)
        
        bank_frame = tk.Frame(parent, bg='#0d1117', relief=tk.RIDGE, bd=2)
        bank_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Total Supply
        supply_label = tk.Label(
            bank_frame,
            text="Total Supply:",
            font=('Arial', 11),
            fg='#8b949e',
            bg='#0d1117'
        )
        supply_label.pack(pady=5)
        
        self.supply_value = tk.Label(
            bank_frame,
            text="1,000,000,000 RDC",
            font=('Arial', 14, 'bold'),
            fg='#00ff88',
            bg='#0d1117'
        )
        self.supply_value.pack()
        
        # RDC Price
        price_label = tk.Label(
            bank_frame,
            text="RDC Price:",
            font=('Arial', 11),
            fg='#8b949e',
            bg='#0d1117'
        )
        price_label.pack(pady=5)
        
        self.rdc_price_value = tk.Label(
            bank_frame,
            text="$1.00 USD",
            font=('Arial', 12, 'bold'),
            fg='#00ff88',
            bg='#0d1117'
        )
        self.rdc_price_value.pack()
        
        # Miner Balance
        balance_label = tk.Label(
            bank_frame,
            text="Miner Balance:",
            font=('Arial', 11),
            fg='#8b949e',
            bg='#0d1117'
        )
        balance_label.pack(pady=5)
        
        self.balance_value = tk.Label(
            bank_frame,
            text="0.00 RDC",
            font=('Arial', 14, 'bold'),
            fg='#ffffff',
            bg='#0d1117'
        )
        self.balance_value.pack()
        
        # USD Value
        usd_label = tk.Label(
            bank_frame,
            text="USD Value:",
            font=('Arial', 11),
            fg='#8b949e',
            bg='#0d1117'
        )
        usd_label.pack(pady=5)
        
        self.usd_value = tk.Label(
            bank_frame,
            text="$0.00 USD",
            font=('Arial', 12, 'bold'),
            fg='#3fb950',
            bg='#0d1117'
        )
        self.usd_value.pack(pady=5)
        
        # Price Sources
        price_source_label = tk.Label(
            bank_frame,
            text="💱 Live Price Sources:",
            font=('Arial', 9),
            fg='#8b949e',
            bg='#0d1117'
        )
        price_source_label.pack(pady=5)
        
        self.price_sources_value = tk.Label(
            bank_frame,
            text="CoinMarketCap, Coinbase, Binance",
            font=('Arial', 8),
            fg='#58a6ff',
            bg='#0d1117'
        )
        self.price_sources_value.pack()
        
    def setup_quantum_panel(self, parent):
        """Setup Quantum Computational State panel"""
        label = tk.Label(
            parent,
            text="🌀 Quantum Experimental Features",
            font=('Arial', 16, 'bold'),
            fg='#a371f7',
            bg='#161b22'
        )
        label.pack(pady=10)
        
        quantum_frame = tk.Frame(parent, bg='#0d1117', relief=tk.RIDGE, bd=2)
        quantum_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Feature activation status
        features_label = tk.Label(
            quantum_frame,
            text="⚠️ EXPERIMENTAL FEATURES (NOT ACTIVATED):",
            font=('Arial', 10, 'bold'),
            fg='#f85149',
            bg='#0d1117'
        )
        features_label.pack(pady=5)
        
        # Computational dimensions with activation status
        self.quantum_5d = self.create_quantum_stat(quantum_frame, "5D Strategy:", "NOT ACTIVATED")
        self.quantum_5d_status = self.create_activation_status(quantum_frame, "Set quantum_5d_strategy=true to enable")
        
        self.quantum_10d = self.create_quantum_stat(quantum_frame, "10D Tornado Conv:", "NOT ACTIVATED")
        self.quantum_10d_status = self.create_activation_status(quantum_frame, "Set quantum_10d_tornado=true to enable")
        
        self.quantum_100d = self.create_quantum_stat(quantum_frame, "100D Fractal Tree:", "NOT ACTIVATED")
        self.quantum_100d_status = self.create_activation_status(quantum_frame, "Set quantum_100d_fractal=true to enable")
        
        self.quantum_1000d = self.create_quantum_stat(quantum_frame, "1000D Waterfall:", "NOT ACTIVATED")
        self.quantum_1000d_status = self.create_activation_status(quantum_frame, "Set quantum_1000d_waterfall=true to enable")
        
        # Real mining mode status
        separator = tk.Frame(quantum_frame, bg='#8b949e', height=2)
        separator.pack(fill=tk.X, padx=10, pady=10)
        
        real_mining_label = tk.Label(
            quantum_frame,
            text="💡 REAL MINING MODE:",
            font=('Arial', 10, 'bold'),
            fg='#ffa657',
            bg='#0d1117'
        )
        real_mining_label.pack(pady=5)
        
        self.real_mining_status = self.create_activation_status(
            quantum_frame, 
            "Set real_mining_mode=true in config.json to activate"
        )
        
        # AI Cypher Status
        cypher_label = tk.Label(
            quantum_frame,
            text="🔐 AI-to-AI Cypher: ACTIVE (Always On)",
            font=('Arial', 10, 'bold'),
            fg='#58a6ff',
            bg='#0d1117'
        )
        cypher_label.pack(pady=10)
        
    def create_activation_status(self, parent, text):
        """Create an activation status label"""
        label = tk.Label(
            parent,
            text=f"    → {text}",
            font=('Arial', 8),
            fg='#8b949e',
            bg='#0d1117',
            anchor='w'
        )
        label.pack(fill=tk.X, padx=10, pady=2)
        return label
        
    def create_quantum_stat(self, parent, label_text, value_text):
        """Create quantum state stat display"""
        container = tk.Frame(parent, bg='#0d1117')
        container.pack(fill=tk.X, padx=10, pady=3)
        
        label = tk.Label(
            container,
            text=label_text,
            font=('Arial', 9),
            fg='#8b949e',
            bg='#0d1117',
            anchor='w'
        )
        label.pack(side=tk.LEFT)
        
        value = tk.Label(
            container,
            text=value_text,
            font=('Arial', 9, 'bold'),
            fg='#a371f7',
            bg='#0d1117',
            anchor='e'
        )
        value.pack(side=tk.RIGHT)
        
        return value
        
    def setup_control_panel(self, parent):
        """Setup control buttons panel"""
        button_frame = tk.Frame(parent, bg='#161b22')
        button_frame.pack(expand=True)
        
        self.start_button = tk.Button(
            button_frame,
            text="▶️ START MINING",
            command=self.start_mining,
            font=('Arial', 12, 'bold'),
            bg='#238636',
            fg='#ffffff',
            activebackground='#2ea043',
            width=15,
            height=2,
            relief=tk.RAISED,
            bd=3
        )
        self.start_button.pack(side=tk.LEFT, padx=10)
        
        self.stop_button = tk.Button(
            button_frame,
            text="⏹️ STOP MINING",
            command=self.stop_mining,
            font=('Arial', 12, 'bold'),
            bg='#da3633',
            fg='#ffffff',
            activebackground='#f85149',
            width=15,
            height=2,
            relief=tk.RAISED,
            bd=3,
            state=tk.DISABLED
        )
        self.stop_button.pack(side=tk.LEFT, padx=10)
        
        status_label = tk.Label(
            button_frame,
            text="Status:",
            font=('Arial', 10),
            fg='#8b949e',
            bg='#161b22'
        )
        status_label.pack(side=tk.LEFT, padx=10)
        
        self.status_value = tk.Label(
            button_frame,
            text="IDLE",
            font=('Arial', 10, 'bold'),
            fg='#f85149',
            bg='#161b22'
        )
        self.status_value.pack(side=tk.LEFT)
        
    def start_mining(self):
        """Start mining operations"""
        if not self.running:
            self.running = True
            self.core.start_mining()
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.status_value.config(text="MINING", fg='#3fb950')
            
            # Start mining thread
            self.mining_thread = threading.Thread(target=self.mining_worker, daemon=True)
            self.mining_thread.start()
            
    def stop_mining(self):
        """Stop mining operations"""
        if self.running:
            self.running = False
            self.core.stop_mining()
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.status_value.config(text="STOPPED", fg='#f85149')
            
    def mining_worker(self):
        """Background mining worker thread"""
        while self.running:
            try:
                self.core.mining_cycle(iterations=100)
                time.sleep(0.1)  # Small delay to prevent CPU overload
            except Exception as e:
                print(f"Mining error: {e}")
                break
                
    def update_ui(self):
        """Update UI with current mining state"""
        try:
            state = self.core.get_dashboard_state()
            config = state.get('config', {})
            experiment = config.get('experiment_features', {})
            
            # Update Bitcoin stats
            btc = state['miners']['bitcoin']
            btc_simulated = config.get('miners', {}).get('bitcoin', {}).get('simulated', True)
            self.btc_price.config(text=f"${btc.get('usd_price', 0.0):,.2f} USD")
            self.btc_mode.config(text="SIMULATION" if btc_simulated else "REAL MINING")
            self.btc_hashrate.config(text=f"{btc['hash_rate']:.2f} H/s")
            self.btc_expected.config(text=f"{btc.get('expected_hashrate', 0):.0f} H/s")
            self.btc_pool.config(text=btc.get('pool_name', 'F2Pool'))
            
            if experiment.get('bitcoin_real_network', False):
                self.btc_real_rate.config(text="ACTIVATED", fg='#3fb950')
            else:
                self.btc_real_rate.config(text="NOT ACTIVATED", fg='#f85149')
            
            self.btc_shares.config(text=str(btc['shares_found']))
            self.btc_hashes.config(text=f"{btc['total_hashes']:,}")
            
            # Update Monero stats
            xmr = state['miners']['monero']
            xmr_simulated = config.get('miners', {}).get('monero', {}).get('simulated', True)
            self.xmr_price.config(text=f"${xmr.get('usd_price', 0.0):,.2f} USD")
            self.xmr_mode.config(text="SIMULATION" if xmr_simulated else "REAL MINING")
            self.xmr_hashrate.config(text=f"{xmr['hash_rate']:.2f} H/s")
            self.xmr_expected.config(text=f"{xmr.get('expected_hashrate', 0):.0f} H/s")
            self.xmr_pool.config(text=xmr.get('pool_name', 'SupportXMR'))
            
            if experiment.get('monero_real_network', False):
                self.xmr_real_rate.config(text="ACTIVATED", fg='#3fb950')
            else:
                self.xmr_real_rate.config(text="NOT ACTIVATED", fg='#f85149')
                
            self.xmr_shares.config(text=str(xmr['shares_found']))
            self.xmr_hashes.config(text=f"{xmr['total_hashes']:,}")
            
            # Update RedCode stats
            rdc = state['miners']['redcode']
            rdc_simulated = config.get('miners', {}).get('redcode', {}).get('simulated', True)
            self.rdc_price.config(text=f"${rdc.get('usd_price', 1.0):.2f} USD")
            self.rdc_mode.config(text="SIMULATION" if rdc_simulated else "REAL MINING")
            self.rdc_hashrate.config(text=f"{rdc['hash_rate']:.2f} H/s")
            self.rdc_expected.config(text=f"{rdc.get('expected_hashrate', 0):.0f} H/s")
            
            # Calculate mined value
            balance = state['rdc_coin']['miner_balance']
            rdc_usd_value = balance * rdc.get('usd_price', 1.0)
            self.rdc_value.config(text=f"${rdc_usd_value:,.2f} USD")
            
            if experiment.get('redcode_quantum_boost', False):
                self.rdc_quantum_boost.config(text="ACTIVATED", fg='#3fb950')
            else:
                self.rdc_quantum_boost.config(text="NOT ACTIVATED", fg='#f85149')
                
            # Show real rate if activated
            if experiment.get('real_mining_mode', False):
                self.rdc_real_rate.config(text="ACTIVATED", fg='#3fb950')
            else:
                self.rdc_real_rate.config(text="NOT ACTIVATED", fg='#f85149')
                
            self.rdc_shares.config(text=str(rdc['shares_found']))
            self.rdc_hashes.config(text=f"{rdc['total_hashes']:,}")
            
            # Update RDC balance and USD value
            balance = state['rdc_coin']['miner_balance']
            usd_value = state['rdc_coin'].get('usd_value', 0.0)
            self.balance_value.config(text=f"{balance:,.2f} RDC")
            self.rdc_price_value.config(text=f"${state['rdc_coin'].get('usd_price', 1.0):.2f} USD")
            self.usd_value.config(text=f"${usd_value:,.2f} USD")
            
            # Update price sources info
            price_sources = state.get('price_sources', {})
            if price_sources.get('last_update'):
                self.price_sources_value.config(
                    text=f"Live: {', '.join(price_sources.get('sources', []))}"
                )
            
            # Update quantum state with activation status
            quantum = state['quantum_state']
            
            if experiment.get('quantum_5d_strategy', False):
                self.quantum_5d.config(text=f"ACTIVE: {quantum['5d']:.6f}", fg='#3fb950')
                self.quantum_5d_status.config(text="    → Quantum 5D Strategy is ENABLED", fg='#3fb950')
            else:
                self.quantum_5d.config(text="NOT ACTIVATED", fg='#f85149')
                self.quantum_5d_status.config(text="    → Set quantum_5d_strategy=true to enable", fg='#8b949e')
            
            if experiment.get('quantum_10d_tornado', False):
                self.quantum_10d.config(text=f"ACTIVE: {quantum['10d']:.6f}", fg='#3fb950')
                self.quantum_10d_status.config(text="    → Quantum 10D Tornado is ENABLED", fg='#3fb950')
            else:
                self.quantum_10d.config(text="NOT ACTIVATED", fg='#f85149')
                self.quantum_10d_status.config(text="    → Set quantum_10d_tornado=true to enable", fg='#8b949e')
            
            if experiment.get('quantum_100d_fractal', False):
                self.quantum_100d.config(text=f"ACTIVE: {quantum['100d']:.6f}", fg='#3fb950')
                self.quantum_100d_status.config(text="    → Quantum 100D Fractal is ENABLED", fg='#3fb950')
            else:
                self.quantum_100d.config(text="NOT ACTIVATED", fg='#f85149')
                self.quantum_100d_status.config(text="    → Set quantum_100d_fractal=true to enable", fg='#8b949e')
            
            if experiment.get('quantum_1000d_waterfall', False):
                self.quantum_1000d.config(text=f"ACTIVE: {quantum['1000d']:.6f}", fg='#3fb950')
                self.quantum_1000d_status.config(text="    → Quantum 1000D Waterfall is ENABLED", fg='#3fb950')
            else:
                self.quantum_1000d.config(text="NOT ACTIVATED", fg='#f85149')
                self.quantum_1000d_status.config(text="    → Set quantum_1000d_waterfall=true to enable", fg='#8b949e')
            
            # Update real mining mode status
            if experiment.get('real_mining_mode', False):
                self.real_mining_status.config(
                    text="    → Real Mining Mode is ENABLED - Connect to actual pools",
                    fg='#3fb950'
                )
            else:
                self.real_mining_status.config(
                    text="    → Set real_mining_mode=true in config.json to activate",
                    fg='#8b949e'
                )
            
        except Exception as e:
            print(f"UI update error: {e}")
            
    def start_update_loop(self):
        """Start the UI update loop"""
        self.update_ui()
        self.root.after(1000, self.start_update_loop)  # Update every second
        

def main():
    """Main entry point for UI application"""
    root = tk.Tk()
    app = MinerDashboardUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
