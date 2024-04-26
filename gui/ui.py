import tkinter as tk
from gui.main_gui import main_gui_class


class ui_class(object):
    def __init__(self):
        self.root = tk.Tk()
        #setup = set_up_class(root)
        self.layout = main_gui_class(self.root)
