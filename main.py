# Resolve text bluryness on Windows Operating System.
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

import os
import argparse

import tkinter as tk
from tkinter import ttk


def on_closing():
    with open('notepad_user_settings_last_window_geometry.txt', 'w') as file:
        window.update()
        file.write(f"{window.winfo_width()}x{window.winfo_height()}")
        print("Closing")
        print(f"{window.winfo_reqwidth()}x{window.winfo_reqheight()}")
        print(f"{window.winfo_width()}x{window.winfo_height()}")
    window.destroy()

def on_window_open(event):
    if os.path.exists('notepad_user_settings_last_window_geometry.txt'):
        with open('notepad_user_settings_last_window_geometry.txt', 'r') as file:
            geometry = file.read()
            window.geometry(geometry)
            window.update()
            print("Window has been opened!")
    else:
        print("No previous settings found.")

# Create main application window
window = tk.Tk()
window.title("Notepad")
window.geometry("800x400")

# Bind the '<Map>' event to the on_window_open function
window.bind('<Map>', on_window_open)

# Define the protocol for the window close button
window.protocol("WM_DELETE_WINDOW", on_closing)

# Create a simple UI
frame = ttk.Frame(window, padding=10)
frame.grid()

ttk.Label(frame, text="Hello World!").grid(column=0, row=0)
ttk.Button(frame, text="Quit", command=on_closing).grid(column=1, row=0)

# Start the Tkinter event loop
window.mainloop()
