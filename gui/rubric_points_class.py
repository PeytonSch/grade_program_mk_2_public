import tkinter as tk
import tkinter.ttk as ttk
import run_configurations as rc
class rubric_points_class(object):
    def __init__(self, master):
        self.rubric = []
        #read in rubric file
        infile = open(rc.rubric_file_path)

        for line in infile:
          if(line.rstrip()):
            self.rubric.append(line)


        #TODO: add scrollbar
        container = ttk.Frame(master)
        canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)


        self.vars = []
        for point in self.rubric:
            var = tk.IntVar(value=1)
            chk = ttk.Checkbutton(scrollable_frame, text=point, variable=var)
            chk.pack(side=tk.TOP, anchor='w', expand=tk.YES)
            self.vars.append(var)

        container.pack(fill="both", expand=True)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        

        
    def reset(self):
      for button in self.vars:
        button.set(1)
    
    
    def state(self):
      return map((lambda var: var.get()), self.vars)

    def export_command(self,comments,student,notes_path):
      grades_string = ""
      notes_string = "====================================="
      grades_file = open(rc.grades_csv_file,'a')

      print("Student: ",student)
      grades_string= grades_string + student + ","
      notes_string= notes_string + '\n' + student + "\n=====================================\n\n"

      print("Comments: ",comments)
      grades_string = grades_string + comments
      notes_string = notes_string + comments

      print("Missed Points: ")

      count = 0
      for rubric_point in self.vars:

        if(rubric_point.get()==0):
          print("Missed: ", self.rubric[count])
          grades_string = grades_string + "Missed: " + self.rubric[count]
          notes_string = notes_string + "Missed: " + self.rubric[count]
        
        count = count + 1
      
      #in append mode, add to student notes file
      with open(notes_path, 'w') as outfile:
                outfile.write(notes_string)

      #add to grades csv
      grades_string = grades_string.replace('\n', "   ")
      grades_string = grades_string.replace('\r', "   ")
      grades_file.write(grades_string)
      grades_file.write('\n')
      grades_file.close()

