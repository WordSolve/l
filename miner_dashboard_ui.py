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
        self.btc_frame = self.create_miner_frame(parent, "Bitcoin (BTC)", "#f7931a")
        self.btc_hashrate = self.create_stat_label(self.btc_frame, "Hash Rate:", "0 H/s")
        self.btc_shares = self.create_stat_label(self.btc_frame, "Shares:", "0")
        self.btc_hashes = self.create_stat_label(self.btc_frame, "Total Hashes:", "0")
        
        # Monero Miner
        self.xmr_frame = self.create_miner_frame(parent, "Monero (XMR)", "#ff6600")
        self.xmr_hashrate = self.create_stat_label(self.xmr_frame, "Hash Rate:", "0 H/s")
        self.xmr_shares = self.create_stat_label(self.xmr_frame, "Shares:", "0")
        self.xmr_hashes = self.create_stat_label(self.xmr_frame, "Total Hashes:", "0")
        
        # RedCode Miner
        self.rdc_miner_frame = self.create_miner_frame(parent, "RedCode (RDC) - Quantum", "#00ff88")
        self.rdc_hashrate = self.create_stat_label(self.rdc_miner_frame, "Hash Rate:", "0 H/s")
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
        self.balance_value.pack(pady=5)
        
    def setup_quantum_panel(self, parent):
        """Setup Quantum Computational State panel"""
        label = tk.Label(
            parent,
            text="🌀 Quantum Computational State",
            font=('Arial', 16, 'bold'),
            fg='#a371f7',
            bg='#161b22'
        )
        label.pack(pady=10)
        
        quantum_frame = tk.Frame(parent, bg='#0d1117', relief=tk.RIDGE, bd=2)
        quantum_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Computational dimensions
        self.quantum_5d = self.create_quantum_stat(quantum_frame, "5D Strategy:", "0.000000")
        self.quantum_10d = self.create_quantum_stat(quantum_frame, "10D Tornado Conv:", "0.000000")
        self.quantum_100d = self.create_quantum_stat(quantum_frame, "100D Fractal Tree:", "0.000000")
        self.quantum_1000d = self.create_quantum_stat(quantum_frame, "1000D Waterfall:", "0.000000")
        
        # AI Cypher Status
        cypher_label = tk.Label(
            quantum_frame,
            text="🔐 AI-to-AI Cypher: ACTIVE",
            font=('Arial', 10, 'bold'),
            fg='#58a6ff',
            bg='#0d1117'
        )
        cypher_label.pack(pady=10)
        
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
            
            # Update Bitcoin stats
            btc = state['miners']['bitcoin']
            self.btc_hashrate.config(text=f"{btc['hash_rate']:.2f} H/s")
            self.btc_shares.config(text=str(btc['shares_found']))
            self.btc_hashes.config(text=f"{btc['total_hashes']:,}")
            
            # Update Monero stats
            xmr = state['miners']['monero']
            self.xmr_hashrate.config(text=f"{xmr['hash_rate']:.2f} H/s")
            self.xmr_shares.config(text=str(xmr['shares_found']))
            self.xmr_hashes.config(text=f"{xmr['total_hashes']:,}")
            
            # Update RedCode stats
            rdc = state['miners']['redcode']
            self.rdc_hashrate.config(text=f"{rdc['hash_rate']:.2f} H/s")
            self.rdc_shares.config(text=str(rdc['shares_found']))
            self.rdc_hashes.config(text=f"{rdc['total_hashes']:,}")
            
            # Update RDC balance
            balance = state['rdc_coin']['miner_balance']
            self.balance_value.config(text=f"{balance:,.2f} RDC")
            
            # Update quantum state
            quantum = state['quantum_state']
            self.quantum_5d.config(text=f"{quantum['5d']:.6f}")
            self.quantum_10d.config(text=f"{quantum['10d']:.6f}")
            self.quantum_100d.config(text=f"{quantum['100d']:.6f}")
            self.quantum_1000d.config(text=f"{quantum['1000d']:.6f}")
            
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
