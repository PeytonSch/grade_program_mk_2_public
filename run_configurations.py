#RUN CONFIGURATIONS ARE VARIABLES THAT WOULD BE CHANGED
#EITHER BETWEEN SETS OR WHEN I REFACTOR MY PROGRAM,
#THINGS LIKE FILE PATHS, RUBRICS, ETC.


#Base Directories
ready_to_grade_path = 'to_grade/ready_to_grade/'
to_canvas_notes_path = 'to_canvas_notes/set6/'

#Students
number_of_students = 56

#Spevific Files

#Set Files
rubric_file_path = './set6_files/set6.txt'

#Default Files
default_user_output = './defaults/default_user_output.txt' #its blank
default_expected_output = './defaults/default_set6.txt' 
welcome_file = './defaults/welcome.txt'
default_image_test_output = './defaults/default_image_output.txt' #no outputs for assignment

#Other Files
error_to_canvas_notes_file = './error_to_canvas_notes.txt' #when no notes found
grades_csv_file = './grades.csv'



#Set specific files
public_test_file = './set6_files/aliceChapter1.txt'
public_read_in_file = './product_public.txt' #students will read in the public file name
private_test_file = './set6_files/Set6_private.txt'
expected_student_output_file = './set6_output.txt' #file we expect students code to produce
#test files
public_test1 = './set6_files/aliceChapter1.out'
private_test1= './set6_files/Set6_private.out'
priavate_test2= './set6_files/greeneggsandham.out'

public_test1_button_name = "Alice Chapter 1"
private_test1_button_name = "Set6 Private"
private_test2_button_name = "Green Eggs and Ham"

#image Test Files
brick_inverted_correct = './set5_files/brick_inverted.ppm'
brick_grey_correct = './set5_files/brick_grey.ppm'
wallpaper_inverted_correct = './set5_files/wallpaper_inverted.ppm'
wallpaper_grey_correct = './set5_files/wallpaper_grey.ppm'
private_inverted_correct = './set5_files/set5private_inverted.ppm'
private_grey_correct = './set5_files/set5private_grey.ppm'

#User Produced Image Files
brick_inverted_user = './b_inverted.ppm'
brick_grey_user = './b_gray.ppm'
wallpaper_inverted_user = './w_inverted.ppm'
wallpaper_grey_user = './w_gray.ppm'
private_inverted_user = './p_inverted.ppm'
private_grey_user = './p_grey.ppm'