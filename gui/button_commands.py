import os
import csv
import run_configurations as rc

def compile_button_command(file_path,viewer, active_tree_path, path,tree):
    run_file = file_path.replace('/','\\')
    string_parts = run_file.rpartition('\\')
    compile_to_path = string_parts[0] + "\\run"
    print('g++ -o '+ compile_to_path + ' .\\' + run_file )
    os.system('g++ -o '+ compile_to_path + ' .\\' + run_file )

    #refresh tree to show file 
    tree.refresh_tree(viewer, active_tree_path, path)


def load_public_test_file():
    with open(rc.public_test_file, 'r') as infile:
            with open(rc.public_read_in_file, 'w') as outfile:
                outfile.write(infile.read())

def load_private_test_file():
    with open(rc.private_test_file, 'r') as infile:
            with open(rc.public_read_in_file, 'w') as outfile:
                outfile.write(infile.read())

def refresh_image_output(viewer):

    #go through all the files and set the answer string to 
    #what is correct or incorrect

    viewer_string = "" #add to this as we go

    #Test Brick Grey
    with open (rc.brick_grey_correct,'r') as correct:
        correct_string = correct.read()
        with open (rc.brick_grey_user,'r') as user:
            user_string = user.read()
            if (correct_string != user_string):
                viewer_string =  viewer_string+ "brick_grey.ppm is not correct\n"
          
    #Test Brick Inverted
    with open (rc.brick_inverted_correct,'r') as correct:
        correct_string = correct.read()
        with open (rc.brick_inverted_user,'r') as user:
            user_string = user.read()
            if (correct_string != user_string):
                viewer_string =  viewer_string+ "brick_inverted.ppm is not correct\n"
    
    #Test Wallpaper Grey
    with open (rc.wallpaper_grey_correct,'r') as correct:
        correct_string = correct.read()
        with open (rc.wallpaper_grey_user,'r') as user:
            user_string = user.read()
            if (correct_string != user_string):
                viewer_string =  viewer_string+ "wallpaper_grey.ppm is not correct\n"
          
    #Test Wallpaper Inverted
    with open (rc.wallpaper_inverted_correct,'r') as correct:
        correct_string = correct.read()
        with open (rc.wallpaper_inverted_user,'r') as user:
            user_string = user.read()
            if (correct_string != user_string):
                viewer_string =  viewer_string+ "wallpaper_inverted.ppm is not correct\n"
    
    #Test Private Grey
    with open (rc.private_grey_correct,'r') as correct:
        correct_string = correct.read()
        with open (rc.private_grey_user,'r') as user:
            user_string = user.read()
            if (correct_string != user_string):
                viewer_string =  viewer_string+ "private_grey.ppm is not correct\n"
          
    #Test Private Inverted
    with open (rc.private_inverted_correct,'r') as correct:
        correct_string = correct.read()
        with open (rc.private_inverted_user,'r') as user:
            user_string = user.read()
            if (correct_string != user_string):
                viewer_string =  viewer_string+ "private_inverted.ppm is not correct\n"
    

    if (viewer_string == ""):
        viewer_string = "All Images Match :D"

    viewer.set_text(viewer_string)

def refresh_student_output(viewer):
    viewer.open_file_and_set_text(rc.expected_student_output_file)

def display_public_output_1(viewer):
    viewer.open_file_and_set_text(rc.public_test1)

def display_private_output_1(viewer):
    viewer.open_file_and_set_text(rc.private_test1)

def display_private_output_2(viewer):
    viewer.open_file_and_set_text(rc.priavate_test2)


def refresh_grades(tree):
    #delete children
    for i in tree.get_children():
        tree.delete(i)
    
    with open(rc.grades_csv_file) as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                print(row)
                student = row['Student']
                comments = row['Comments']
                tree.insert("", 0, values=(student, comments))



    
