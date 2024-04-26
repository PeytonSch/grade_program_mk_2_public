import tkinter as tk
import tkinter.ttk as ttk

class progress_bar_class(object):
    def __init__(self, master, length):
        self.progress = ttk.Progressbar(master,length=length,  mode='determinate')
        self.progress.pack()


    def update_progress(self, master, value):
        self.progress['value'] = value
        master.update_idletasks()
