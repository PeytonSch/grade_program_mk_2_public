import csv
import os
import tkinter as tk
import tkinter.ttk as ttk


import run_configurations as rc

from gui.bar import progress_bar_class
from gui.button_commands import *
from gui.file_viewer import file_viewer_class
from gui.notebook_class import notebook_class
#from style import *
from gui.rubric_points_class import rubric_points_class
from gui.student_info import student_info_class
from gui.tree import tree_window_class


class main_gui_class(object):
    def __init__(self, root):

        #OUTERMOST PROGRAM

#window geometry
        #root.geometry("1200x900+50+50")
        self.w, self.h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry("%dx%d+0+0" % (self.w, self.h))
        root.title('Peyton Scherschel\'s 261 Grading Program')

        self.row1_height = 600

#misc variables
        self.current_test_file = rc.default_expected_output
        self.user_output = rc.default_user_output

        self.image_output = rc.default_image_test_output

        self.total_students_to_grade = rc.number_of_students
        self.student_folders_in_dir = self.get_all_submitted_folders()

        #just used at start of program to display the welcome screen
        self.welcome_file = rc.welcome_file

        self.student_control_number = 0
        self.active_student_folder = self.student_folders_in_dir[self.student_control_number]
        self.active_tree_path = rc.ready_to_grade_path + self.active_student_folder
        self.active_notes_path = rc.to_canvas_notes_path+ self.active_student_folder + '.txt'


        self. student_number = "1"
        self.student_number_string = self.active_student_folder + " Student Number: " + self.student_number

        #OUTSIDE NOTEBOOK WINDOW
        self.notebook = notebook_class(root)

#NOTEBOOK WINDOWS
        self.output_window = ttk.Frame(self.notebook.get_notebook())
        self.image_window = ttk.Frame(self.notebook.get_notebook())
        self.home_window = ttk.Frame(self.notebook.get_notebook())
        self.grades_file_window = ttk.Frame(self.notebook.get_notebook())
        self.to_canvas_window = ttk.Frame(self.notebook.get_notebook())
        self.notebook.add_window(self.home_window, 'Home Window')
        self.notebook.add_window(self.output_window, 'Text Output Viewer')
        self.notebook.add_window(self.image_window, 'Image Output Tester')
        self.notebook.add_window(self.grades_file_window, 'Grades')
        self.notebook.add_window(self.to_canvas_window,"To Canvas")
        
#Columns and Weights
        self.home_window.columnconfigure(0,weight=1)
        self.home_window.columnconfigure(1,weight=2)
        self.home_window.columnconfigure(3,weight=3)
        self.home_window.rowconfigure(0,weight=5)
        self.home_window.rowconfigure(1,weight=1)
        self.home_window.rowconfigure(2,weight=3)

        self.output_window.columnconfigure(0,weight=1)
        self.output_window.columnconfigure(1,weight=1)
        self.output_window.rowconfigure(0,weight=1)
        self.output_window.rowconfigure(1,weight=60)

        self.image_window.columnconfigure(0,weight=1)
        self.image_window.columnconfigure(1,weight=1)
        self.image_window.rowconfigure(0,weight=1)
        self.image_window.rowconfigure(1,weight=60)

        self.grades_file_window.columnconfigure(0,weight=1)
        self.grades_file_window.rowconfigure(0,weight=1)

        self.to_canvas_window.columnconfigure(0,weight=1)
        self.to_canvas_window.rowconfigure(0,weight=9)
        self.to_canvas_window.rowconfigure(1,weight=1)
        self.to_canvas_window.rowconfigure(2,weight=1)
    
#Output Window Items
        #Output Window Frames
        self.expected_output_frame = ttk.LabelFrame(self.output_window, text="Expected Output")
        self.expected_output_frame['relief'] = 'groove'
        self.expected_output_frame.grid(column=0,row=1, sticky="n,s,e,w")

        self.user_output_frame = ttk.LabelFrame(self.output_window, text="User Output")
        self.user_output_frame['relief'] = 'groove'
        self.user_output_frame.grid(column=1,row=1, sticky="n,s,e,w")

        self.output_window_buttons_frame = ttk.LabelFrame(self.output_window, text="Commands")
        self.output_window_buttons_frame['relief'] = 'groove'
        self.output_window_buttons_frame.grid(columnspan=2,row=0, sticky="n,s,e,w")

        #Output Window Refresh Button
        self.refresh_output_window_button = ttk.Button(self.output_window_buttons_frame, text="Refresh", command=lambda :refresh_student_output(self.user_output_file_viewer))
        self.refresh_output_window_button.pack()
        self.output_display_label = ttk.Label(self.output_window_buttons_frame, text=self.current_test_file)
        self.output_display_label.pack()

        #Output Window Change Output Cases
        self.output_window_buttons_frame2 = ttk.LabelFrame(self.output_window_buttons_frame, text="Change Test Cases")
        self.output_window_buttons_frame2['relief'] = 'groove'
        self.output_window_buttons_frame2.pack()

        #Output Window Expected Output  
        self.expected_output_file_viewer = file_viewer_class(self.expected_output_frame, self.current_test_file)
        self.user_output_file_viewer = file_viewer_class(self.user_output_frame, self.user_output)

        #Change Output Buttons
        self.output_window_show_out1_button = ttk.Button(self.output_window_buttons_frame, text=rc.public_test1_button_name,command=lambda :display_public_output_1(self.expected_output_file_viewer))
        self.output_window_show_out1_button.pack(side='left')
        self.output_window_show_out2_button = ttk.Button(self.output_window_buttons_frame, text=rc.private_test1_button_name, command= lambda :display_private_output_1(self.expected_output_file_viewer))
        self.output_window_show_out2_button.pack(side='left')
        self.output_window_show_out3_button = ttk.Button(self.output_window_buttons_frame, text=rc.private_test2_button_name, command= lambda :display_private_output_2(self.expected_output_file_viewer))
        self.output_window_show_out3_button.pack(side='left')

        
#Image Window Items

        #Image Window Frames
        self.expected_image_output_frame = ttk.LabelFrame(self.image_window, text="Expected Output Image")
        self.expected_image_output_frame['relief'] = 'groove'
        self.expected_image_output_frame.grid(column=0,row=1, rowspan=2, sticky="n,s,e,w")

        #self.user_image_output_frame = ttk.LabelFrame(self.image_window, text="User Output Image")
        #self.user_image_output_frame['relief'] = 'groove'
        #self.user_image_output_frame.grid(column=1,row=1, sticky="n,s,e,w")

        self.image_window_buttons_frame = ttk.LabelFrame(self.image_window, text="Commands")
        self.image_window_buttons_frame['relief'] = 'groove'
        self.image_window_buttons_frame.grid(columnspan=2,row=0, sticky="n,s,e,w")
        
        #Output Window Expected Output  
        self.image_test_file_viewer = file_viewer_class(self.expected_image_output_frame, self.image_output)

        #Image Window Test Button
        self.test_all_images_button = ttk.Button(self.image_window_buttons_frame, text="Test All", command=lambda :refresh_image_output(self.image_test_file_viewer))
        self.test_all_images_button.pack()    




#Home Window Items
    #Frames and Windows
        #INNER WINDOW LAYOUT
        self.left_frame = ttk.LabelFrame(self.home_window, text="Directory",height=self.row1_height,width=200)
        self.left_frame['relief'] = 'groove'
        self.left_frame.grid(column=0,row=0, sticky="n,s,e,w")

        self.middle_frame = ttk.LabelFrame(self.home_window, text="Viewer",height=self.row1_height,width=675)
        self.middle_frame['relief'] = 'groove'
        self.middle_frame.grid(column=1,row=0, sticky="n,s,e,w")

        self.right_frame = ttk.LabelFrame(self.home_window, text="Rubric Points",height=self.row1_height,width=200)
        self.right_frame['relief'] = 'groove'
        self.right_frame.grid(column=3,row=0, sticky="n,s,e,w")



        #File Viewer
        self.file_viewer = file_viewer_class(self.middle_frame, self.welcome_file)

        #TREE WINDOWS
        self.home_tree = tree_window_class(self.left_frame, self.file_viewer,self.active_tree_path, path=self.active_tree_path)

        #RUBRIC POINTS
        self.rubric_points = rubric_points_class(self.right_frame)



        self.mid_bottom_frame = ttk.LabelFrame(self.home_window, text="Mid Bot Frame",height=125,width=675)
        self.mid_bottom_frame['relief'] = 'groove'
        self.mid_bottom_frame.grid(row=1,column=0, columnspan=4, sticky="n,s,e,w")



        self.bottom_frame = ttk.LabelFrame(self.home_window, text="Bot Frame",height=75,width=850)
        self.bottom_frame['relief'] = 'groove'
        self.bottom_frame.grid(row=2, column=0, columnspan=4, sticky="n,s,e,w")


        #Student Info
        self.student_info = student_info_class(self.mid_bottom_frame, self.student_number_string)
        #Progress Bar
        self.progress_bar = progress_bar_class(self.mid_bottom_frame,
            length = 700)

        #set a value to start just to show
        self.progress_bar.update_progress(self.mid_bottom_frame,0)

    #Buttons and Comments Box
        #MID-BOTTOM FRAME COMMAND BUTTONS
        self.export_csv = ttk.Button(self.mid_bottom_frame, text="Export Student", command=lambda :self.rubric_points.export_command(self.comments_box.get("1.0",tk.END),self.active_student_folder,self.active_notes_path))
        self.export_csv.pack(side='right')

        self.load_test_file1_button = ttk.Button(self.mid_bottom_frame, text="Load Public Test File", command= load_public_test_file)
        self.load_test_file1_button.pack(side='left')

        self.load_test_file2_button = ttk.Button(self.mid_bottom_frame, text="Load Private Test File", command= load_private_test_file)
        self.load_test_file2_button.pack(side='left')

        #BOTTOM FRAME COMMAND BUTTONS
        self.next_student_button = ttk.Button(self.bottom_frame, text="Next Student", command = self.next_student_command)
        self.next_student_button.pack(side='right')

        self.prev_student_button = ttk.Button(self.bottom_frame, text="Previous Student", command = self.prev_student_command)
        self.prev_student_button.pack(side='left')

        self.save_file_button = ttk.Button(self.bottom_frame, text="Save File", command=lambda :self.file_viewer.save_button_command(self.middle_frame,self.home_tree.getActiveFile(self.active_tree_path)))
        self.save_file_button.pack(side='left')

        self.compile_button = ttk.Button(self.bottom_frame, text="Compile Current File", command=lambda : compile_button_command(self.home_tree.getActiveFile(self.active_tree_path),self.file_viewer,self.active_tree_path, self.active_tree_path,self.home_tree))
        self.compile_button.pack(side='right')

        #comments box
        self.comments_box = tk.Text(self.bottom_frame,height=5)
        self.comments_box.pack()






        #GRADES WINDOW STUFF

        self.refresh_grades_button = ttk.Button(self.grades_file_window, text="Refresh", command=lambda : refresh_grades(self.grades_table))    
        self.refresh_grades_button.pack(side='top')


        self.TableMargin = tk.Frame(self.grades_file_window, width=self.w-200)
        self.TableMargin.pack(side='bottom')

        scrollbarx = tk.Scrollbar(self.TableMargin, orient=tk.HORIZONTAL)
        scrollbary = tk.Scrollbar(self.TableMargin, orient=tk.VERTICAL)
        self.grades_table = ttk.Treeview(self.TableMargin, columns=("Student", "Comments"), height=self.h-600, selectmode="extended",
                            yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=self.grades_table.yview)
        scrollbary.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbarx.config(command=self.grades_table.xview)
        scrollbarx.pack(side=tk.BOTTOM, fill=tk.X)
        self.grades_table.heading('Student', text="Student", anchor=tk.W)
        self.grades_table.heading('Comments', text="Comments", anchor=tk.W)
        self.grades_table.column('#0', stretch=tk.YES, minwidth=0, width=0)
        self.grades_table.column('#1', stretch=tk.YES, minwidth=0, width=300)
        self.grades_table.column('#2', stretch=tk.YES, minwidth=0, width=700)

        

        self.grades_table.pack()
        with open(rc.grades_csv_file) as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                student = row['Student']
                comments = row['Comments']
                self.grades_table.insert("", 0, values=(student, comments))



        #to_canvas stuff
        self.to_canvas_notes_frame = ttk.LabelFrame(self.to_canvas_window,text="To Canvas")
        self.to_canvas_notes_frame.grid(row=0, column=0, sticky="n,s,e,w")
        self.to_canvas_progress_frame = ttk.LabelFrame(self.to_canvas_window,text="Current Student")
        self.to_canvas_progress_frame.grid(row=1, column=0, sticky="n,s,e,w")
        self.to_canvas_commands_frame = ttk.LabelFrame(self.to_canvas_window,text="Commands")
        self.to_canvas_commands_frame.grid(row=2, column=0, sticky="n,s,e,w")


        #Student Info
        self.student_info_to_canvas = student_info_class(self.to_canvas_progress_frame, self.student_number_string)

        #Progress Bar
        self.progress_bar_to_canvas = progress_bar_class(self.to_canvas_progress_frame,
            length = 700)

        #set a value to start just to show
        self.progress_bar_to_canvas.update_progress(self.to_canvas_progress_frame,0)

        #Command Buttons
        self.next_student_button_to_canvas = ttk.Button(self.to_canvas_commands_frame, text="Next Student", command = self.next_student_command)
        self.next_student_button_to_canvas.pack(side='right')

        self.prev_student_button_to_canvas = ttk.Button(self.to_canvas_commands_frame, text="Previous Student", command = self.prev_student_command)
        self.prev_student_button_to_canvas.pack(side='left')

        self.save_file_button_to_canvas = ttk.Button(self.to_canvas_commands_frame, text="Save File", command=lambda :self.file_viewer_to_canvas.save_button_command(self.to_canvas_notes_frame,self.active_notes_path))
        self.save_file_button_to_canvas.pack(side='left')

        #Notes Frame:
        if os.path.exists(self.active_notes_path):
            self.to_canvas_file = self.active_notes_path
        else:
            print("Could Not Find Path: ",self.active_notes_path)
            with open(rc.error_to_canvas_notes_file, 'w') as outfile:
                error_string = "Could Not Find Notes For:    " + self.student_number_string
                outfile.write(error_string)
            self.to_canvas_file = rc.error_to_canvas_notes_file
        self.file_viewer_to_canvas = file_viewer_class(self.to_canvas_notes_frame,self.to_canvas_file)

        #refresh the to canvas window when tabs are changed
        self.notebook.bind_tab_changes(self.file_viewer_to_canvas,self.active_notes_path,self.student_number_string)











        #DISABLE ITEMS FOR CURRENT SET
        #self.refresh_output_window_button.configure(state=tk.DISABLED)
        #self.output_window_show_out1_button.configure(state=tk.DISABLED)
        #self.output_window_show_out2_button.configure(state=tk.DISABLED)
        #self.output_window_show_out3_button.configure(state=tk.DISABLED)
        #self.load_test_file1_button.configure(state=tk.DISABLED)
        #self.load_test_file2_button.configure(state=tk.DISABLED)

        #Main Loop
        root.mainloop()

#Functions
    def next_student_command(self):
        self.student_control_number = self.student_control_number + 1
        self. student_number = str(self.student_control_number+1)
        self.new_student()

    def prev_student_command(self):
        self.student_control_number = self.student_control_number - 1
        self. student_number = str(self.student_control_number+1)
        self.new_student()
    
    def get_all_submitted_folders(self):
        folders = next(os.walk(rc.ready_to_grade_path))[1]
        return folders

    def new_student(self):
        #RESET STUDENT INFO VARIABLES
        self.active_student_folder = self.student_folders_in_dir[self.student_control_number]
        self.active_tree_path = rc.ready_to_grade_path+ self.active_student_folder
        self.student_number_string = self.active_student_folder + " Student Number: " + self.student_number
        self.active_notes_path = rc.to_canvas_notes_path + self.active_student_folder + '.txt'
        #RESET COMMENTS BOX
        self.comments_box.delete("1.0",tk.END)

        #RESET CHECKBOXES
        self.rubric_points.reset()

        #RESET TREE VIEW
        self.home_tree.refresh_tree(self.file_viewer,self.active_tree_path,self.active_tree_path)

        #RESET VIEWER TO WELCOME SCREEN
        self.file_viewer.open_file_and_set_text(rc.welcome_file)

        #SET TO_CANVAS VIEWER TO NEXT STUDENT NOTES
        self.file_viewer_to_canvas.check_for_new_students_notes(self.active_notes_path,self.student_number_string)

        #RESET STUDENT GRADE STING TOOLTIPS
        self.student_info.set_to_new_student(self.student_number_string)
        self.student_info_to_canvas.set_to_new_student(self.student_number_string)

        #UPDATE POGRESS BARS
        self.progress_bar.update_progress(self.mid_bottom_frame,((self.student_control_number/self.total_students_to_grade)*100))
        self.progress_bar_to_canvas.update_progress(self.to_canvas_progress_frame,((self.student_control_number/self.total_students_to_grade)*100))

        #rebind tab change?
        self.notebook.bind_tab_changes(self.file_viewer_to_canvas,self.active_notes_path,self.student_number_string)