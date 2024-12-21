import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class MarginCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Margin Calculator")
        self.root.geometry("500x600")
        
        style = ttk.Style()
        style.configure("TLabel", padding=5, font=('Helvetica', 10))
        style.configure("TButton", padding=5, font=('Helvetica', 10))
        style.configure("TEntry", padding=5)
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Input fields
        ttk.Label(main_frame, text="Total Equity ($):").grid(row=0, column=0, sticky=tk.W)
        self.equity_var = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.equity_var).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(main_frame, text="Margin Used ($):").grid(row=1, column=0, sticky=tk.W)
        self.margin_var = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.margin_var).grid(row=1, column=1, padx=5, pady=5)
        
        # Calculate button
        ttk.Button(main_frame, text="Calculate", command=self.calculate).grid(row=2, column=0, columnspan=2, pady=20)
        
        # Results display
        self.results_frame = ttk.LabelFrame(main_frame, text="Results", padding="10")
        self.results_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        # Results labels
        self.labels = {}
        results_fields = [
            "Free Margin", "Total Position Size", "Current Margin Level",
            "Drop to Zero Free Margin", "Drop to 80% Margin", "Drop to 50% Margin"
        ]
        
        for i, field in enumerate(results_fields):
            ttk.Label(self.results_frame, text=f"{field}:").grid(row=i, column=0, sticky=tk.W)
            self.labels[field] = ttk.Label(self.results_frame, text="")
            self.labels[field].grid(row=i, column=1, sticky=tk.W)

    def calculate(self):
        try:
            total_equity = float(self.equity_var.get())
            margin_used = float(self.margin_var.get())
            
            # Calculations
            free_margin = total_equity - margin_used
            total_position_size = margin_used * 5
            current_margin_level = (total_equity / margin_used) * 100
            
            drop_to_zero_margin = free_margin
            drop_to_80_percent = total_equity - (margin_used * 0.8)
            drop_to_50_percent = total_equity - (margin_used * 0.5)
            
            drop_percentage = (drop_to_zero_margin / total_position_size) * 100
            drop_80_percentage = (drop_to_80_percent / total_position_size) * 100
            drop_50_percentage = (drop_to_50_percent / total_position_size) * 100
            
            # Update results
            self.labels["Free Margin"].config(text=f"${free_margin:,.2f}")
            self.labels["Total Position Size"].config(text=f"${total_position_size:,.2f}")
            self.labels["Current Margin Level"].config(text=f"{current_margin_level:.2f}%")
            self.labels["Drop to Zero Free Margin"].config(text=f"${drop_to_zero_margin:,.2f} ({drop_percentage:.2f}%)")
            self.labels["Drop to 80% Margin"].config(text=f"${drop_to_80_percent:,.2f} ({drop_80_percentage:.2f}%)")
            self.labels["Drop to 50% Margin"].config(text=f"${drop_to_50_percent:,.2f} ({drop_50_percentage:.2f}%)")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")

def main():
    root = tk.Tk()
    app = MarginCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
