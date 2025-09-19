import sys
import os
from modules.mod_add_date import add_date
from modules.mod_view_date import view_date
from modules.mod_delete_line import delete_line
from modules.mod_reset import reset
from modules.mod_menu_settings import menu_settings
from modules.mod_input_data import input_data
from modules.mod_check_enter import check_enter
from modules.mod_check_escape import check_escape

import msvcrt

def menu():
    '''
    Shows user the menu for application

    Returns:
    --------
    menu (function) : calls itself (keeps application running) until option 4 is selected by the user
    '''
    
    delete_line(100)

    print("***V1 Period App*** \n 1: Record Period Start Date \n 2: View Next Period Date \n 3: Settings \n 4: Quit \nChoose one of the options above:")
    choice = input_data("numbers")

    if check_enter(choice, 100) or check_escape(choice): #or conditional since either option returns same menu, the main one
        return menu()

    choice = int(choice)    #convert input to digit for boolean comparisons

    if choice == 1:
        delete_line(10) #delete irrelevant lines from main menu
        output = add_date() #function call and assign return value
    elif choice == 2:
        delete_line(10)
        output = view_date()
    elif choice == 3:
        delete_line(10)
        output = menu_settings()
    elif choice == 4:
        delete_line(10)   #clearing menu before exiting program
        print("***You have quit the application.***")
        sys.exit(0) #command to exit program, 0 to avoid throwing exception
    else:
        output = "Please choose a valid option."

    if output == "previous":    #condition to skip user input (no information on screen to consider, result from escape during input of date)
        delete_line(100)
        return menu()
    else:
        print(output)
        reset(100) #clear screen after each application use, waits for user input of enter of escape
        return menu()