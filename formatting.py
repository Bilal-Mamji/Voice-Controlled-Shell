import math
#This file contains functions needed for formatting

#this function add the break line
def line(size = 81):
    print(''.ljust(size, '='))
    return

#this function will enclose the text in a box
def text_box(mytext, size = 81):
    start = 0
    end = size - 4
    no_of_lines = math.ceil(len(mytext)/end)
    line(size)
    for i in range(no_of_lines):
        print('| ' + mytext[start:end].ljust(size - 4, ' ') + ' |')
        start = start + end
        end = end + end
    line(size)
    return

#this function will add the heading
def head(mytext, size = 86):
    line(size)
    print('|' + mytext.center(size - 4, ' ') + '|')
    line(size)
    return

#this function will add the heading of a table
def table_head(itemNo, left_text, right_text, left_size = 20, right_size = 50):
    size = 5 + left_size + right_size + 7
    line(size)
    print('| ' + itemNo.center(3, ' ') + '| ' + left_text.center(left_size, ' ') + ' | ' + right_text.center(right_size, ' ') + ' |')
    line(size)
    return

#this function will add the contents of the table
def table_content(itemNo, left_text, right_text, left_size = 20, right_size = 50):
    size = 5 + left_size + right_size + 7
    print('| ' + itemNo.ljust(3, ' ') + '| ' + left_text.ljust(left_size, ' ') + ' | ' + right_text.ljust(right_size, ' ') + ' |')
    line(size)
    return


#this function will print out the welcome window
def show_list():
    table_head('No', 'Command', 'Description')
    table_content('1', 'Send Email', 'Can send mails to several receivers')
    table_content('2', 'Weather Update', 'Will display the current weather Report')
    table_content('3', 'List Files', 'Will List files of current Directory')
    table_content('4', 'Date', "Today's date will be displayed")
    table_content('5', 'time', 'Shows current time')
    table_content('6', 'What is the Day', 'Shows the name of the day') 
    table_content('7', 'Calender', 'Shows Calender')
    table_content('8', 'Shutdown', 'The computer will be powered off')
    table_content('9', 'Reboot', 'The computer will restart')
    table_content('10', 'Create File', 'New file will be created in the current folder')
    table_content('11', 'Create Folder', 'New folder will be created in the current folder')
    table_content('12', 'File type', 'The file information will be displayed')
    table_content('13', 'Create User', 'The new user will be created.')
    table_content('14', 'Delete User', 'Deletes the user.')
    table_content('15', 'Root User', 'Login as Root User')
    table_content('16', 'Current Directory', 'Current working Directory will be displayed')
    table_content('17', 'Create Directory', 'New Directory will be created')
    table_content('18', 'Go Back', 'Move to the previous directory')
    table_content('19', 'Change Directory', 'Move to the specified directory')
    table_content('20', 'Delete file', 'Deletes the specified file')
    table_content('21', 'Delete Directory', 'Deletes the specified directory')
    table_content('22', 'Open Youtube', 'Opens youtube in Web browser')
    table_content('23', 'Open Google', 'Opens google in Web browser')
    table_content('24', 'Open Facebook', 'Opens facebook in Web browser')
    table_content('25', 'Open Firefox', 'Opens firefox in Web browser')
    table_content('26', 'Close Firefox', 'Close firefox in Web browser')
    table_content('27', 'Username', 'Shows current Username')
    table_content('28', 'Who is your Owner', 'Shows name of the Owners')
    table_content('29', 'Clear', 'Clear Screen')
    table_content('30', 'Exit', 'Exit the program')
    
    return
