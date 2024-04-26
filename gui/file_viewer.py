import tkinter as tk
import tkinter.ttk as ttk
import os
import run_configurations as rc

class file_viewer_class(object):
    def __init__(self, master, infile):

        self.text_area = tk.Text(master, wrap='word')
        with open(infile, 'r') as f:
            self.text_area.insert(tk.INSERT, f.read())
        self.text_area.pack(fill="both",expand=True)

    # def refresh(self,master,infile):
    #     self.text_area = tk.Text(master, wrap='word')
    #     with open(infile, 'r') as f:
    #         self.text_area.insert(tk.INSERT, f.read())
    #     self.text_area.pack(fill="both",expand=True)

    def read_text(self):
        return self.text_area.get("1.0",tk.END)

    def set_text(self,text):
        self.text_area.delete("1.0",tk.END)
        self.text_area.insert("1.0",text)

    def save_button_command (self,master,outfile_path):
        #get text from viewer
        read_text = self.read_text()
        #write text out to file
        outfile = open(outfile_path,'w')
        outfile.writelines(read_text)
        #refresh text in viewer to show updated file
        self.set_text(read_text)

    def open_file_and_set_text(self, infile):
        self.text_area.delete("1.0",tk.END)
        with open(infile, 'r') as f:
            self.text_area.insert(tk.INSERT, f.read())

    def check_for_new_students_notes(self,path,student):
        if os.path.exists(path):
            to_canvas_file = path
        else:
            with open(rc.error_to_canvas_notes_file, 'w') as outfile:
                error_string = "Could Not Find Notes For:    " + student
                outfile.write(error_string)
            to_canvas_file = rc.error_to_canvas_notes_file
        
        self.open_file_and_set_text(to_canvas_file)