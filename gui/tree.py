import os
import tkinter as tk
import tkinter.ttk as ttk


class tree_window_class(object):
    def __init__(self, master, viewer,active_tree_path, path):
        self.nodes = dict()
        frame = tk.Frame(master)
        self.tree = ttk.Treeview(frame)
        #ysb = ttk.Scrollbar(frame, orient='vertical', command=self.tree.yview)
        #xsb = ttk.Scrollbar(frame, orient='horizontal', command=self.tree.xview)
        #self.tree.configure(yscroll=ysb.set, xscroll=xsb.set)
        self.tree.heading('#0', text='Project tree', anchor='w')

        self.tree.pack(fill="both",expand=True)
        #ysb.grid(row=0, column=1, sticky='ns')
        #xsb.grid(row=1, column=0, sticky='ew')
        frame.pack(fill="both", expand=True)

        abspath = os.path.abspath(path)
        self.insert_node('', abspath, abspath)
        self.tree.bind('<<TreeviewOpen>>', self.open_node)
        self.tree.bind("<Double-1>", lambda event: self.OnDoubleClick(event,viewer,active_tree_path))


    def refresh_tree(self,viewer, active_tree_path, path):
        #delete children
        for i in self.tree.get_children():
           self.tree.delete(i)

        abspath = os.path.abspath(path)
        self.insert_node('', abspath, abspath)
        self.tree.bind('<<TreeviewOpen>>', self.open_node)
        self.tree.bind("<Double-1>", lambda event: self.OnDoubleClick(event,viewer,active_tree_path))

    def insert_node(self, parent, text, abspath):
        node = self.tree.insert(parent, 'end', text=text, open=False)
        if os.path.isdir(abspath):
            self.nodes[node] = abspath
            self.tree.insert(node, 'end')

    def open_node(self, event):
        node = self.tree.focus()
        abspath = self.nodes.pop(node, None)
        if abspath:
            self.tree.delete(self.tree.get_children(node))
            for p in os.listdir(abspath):
                self.insert_node(node, p, os.path.join(abspath, p))


    #IS NOT WORKING AND NOT USED
    # def open_children(self,parent):
    #     self.tree.item(parent,open=True)
    #     for child in self.tree.get_children(parent):
    #         self.open_children(child)

    # def open_all_nodes(self,event):
    #     self.open_children(self.tree.focus())


    def getActiveFile(self,active_tree_path):
        item_iid = self.tree.selection()[0]
        file_name = self.tree.item(item_iid,"text")
        lab_folder_iid = self.tree.parent(item_iid)
        lab_folder = self.tree.item(lab_folder_iid,"text")
        assignment_folder_iid = self.tree.parent(lab_folder_iid)
        assignment_folder = self.tree.item(assignment_folder_iid,"text")

        path = assignment_folder+"/"+lab_folder+"/"+file_name

        #print("PATH:",path)
        active_file = active_tree_path + "/" + path

        return active_file

    def getFileName(self,active_tree_path):
        item_iid = self.tree.selection()[0]
        file_name = self.tree.item(item_iid,"text")

        return file_name

    def OnDoubleClick(self, event, viewer,active_tree_path):
        active_file = self.getActiveFile(active_tree_path)
        file_name = self.getFileName(active_tree_path)
        #print("File name: ", active_file)
        start = 0
        for c in range(len(file_name)):
            if (file_name[c] == '.'):
                start = c
        file_extension = file_name[start:]

        #print(file_extension)

        if (file_extension == ".cpp" or file_extension == ".txt"):
            viewer.open_file_and_set_text(active_file)
        elif (file_extension == ".exe"):

            #use this line if running from git bash
            #run_file = active_file.replace('/','\\\\')

            #use this line if running from powershell
            run_file = active_file.replace('/','\\')
            run_file = '.\\'+ run_file

            print("Running: ",run_file)
            os.system(run_file)
