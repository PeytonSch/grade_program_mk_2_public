import tkinter as tk
import tkinter.ttk as ttk

class student_info_class(object):
    def __init__(self, master,text):
        self.label=tk.Label(master,text=text)
        self.label.pack()
    
    def set_to_new_student(self,student_text_string):
        self.label.config(text = student_text_string)
