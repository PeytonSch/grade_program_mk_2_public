import tkinter as tk
import tkinter.ttk as ttk

# Initialize style
style = ttk.Style()
# Create style used by default for all Frames
style.configure('TFrame', background='green')
# Other styles
style.configure('Frame1.TFrame', background='red')
style.configure('Frame2.TFrame', background='blue')
