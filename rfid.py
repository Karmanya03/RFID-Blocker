#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, messagebox

def block_rfid():
    # Simulate RFID blocking action
    messagebox.showinfo("RFID Blocker", "RFID signals are being blocked!")

def unblock_rfid():
    # Simulate RFID unblocking action
    messagebox.showinfo("RFID Blocker", "RFID signals are no longer blocked.")

# Create main application window
root = tk.Tk()
root.title("Advanced RFID Blocker")
root.geometry("400x300")
root.resizable(False, False)

# Modern theme using ttk
style = ttk.Style()
style.theme_use('clam')

# Add some styling
style.configure('TButton', font=('Helvetica', 12))
style.configure('TLabel', font=('Helvetica', 14), padding=10)
style.configure('TFrame', background='#f0f0f0')

main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Title Label
title_label = ttk.Label(main_frame, text="RFID Blocker Simulation", font=('Helvetica', 16, 'bold'))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Block RFID Button
block_button = ttk.Button(main_frame, text="Block RFID", command=block_rfid)
block_button.grid(row=1, column=0, pady=20, padx=10)

# Unblock RFID Button
unblock_button = ttk.Button(main_frame, text="Unblock RFID", command=unblock_rfid)
unblock_button.grid(row=1, column=1, pady=20, padx=10)

# Start the GUI event loop
root.mainloop()
