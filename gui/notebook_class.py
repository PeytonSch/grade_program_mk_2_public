import tkinter as tk
import tkinter.ttk as ttk

class notebook_class(object):
    def __init__(self, master):
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(expand = 1, fill ="both")

    def add_window(self,window,text_label ):
        self.notebook.add(window, text = text_label)


    def get_notebook(self):
        return self.notebook

    def bind_tab_changes(self,viewer,notes_path,student_number_string):
        print("tab changed")
        self.notebook.bind("<<NotebookTabChanged>>" , lambda event: self.refresh_notes(event,viewer,notes_path,student_number_string))
        
    def refresh_notes(self,event,viewer,notes_path,student_number_string):

        #do something if to canvas tab is selected
        if(self.notebook.tab("current")['text'] == "To Canvas"):
            viewer.check_for_new_students_notes(notes_path,student_number_string)
