from modules.mod_delete_line import delete_line
from modules.mod_input_data import input_data
from modules.mod_add_notif import add_notif
from modules.mod_update_notif import update_notif
from modules.mod_delete_notif import delete_notif
from modules.mod_reset import reset
from modules.mod_read_contact import read_contact
from modules.mod_add_contact import add_contact
from modules.mod_check_enter import check_enter
from modules.mod_check_escape import check_escape

def menu_notif():
    '''
    Shows user the menu for notifications

    Returns
    --------
    add_contact (function) : call this function if user has not yet given contact information
    menu_notif (function) : calls itself when a valid option is not given by user or when user chooses this option
    output (string) : assigns string to allow escape to previous menu level (settings)
    '''

    delete_line(100)

    contactInfo = read_contact()
    if len(contactInfo[0]) == 0:    #control structure to prevent setting notifications without adding contact information
        print("You have not setup your contact information. You must do this before setting up your notifications.")
        reset(100)
        return add_contact()    #move directly to add contact flow, skipping menu

    output = ""

    print("***Notifications*** \n 1: Add \n 2: Update \n 3: Delete \nChoose one of the options above.")
    choice = input_data("numbers")

    if check_enter(choice, 100):
        return menu_notif()
    elif check_escape(choice):
        output = check_escape(choice)[1]
        return output

    choice = int(choice)

    if choice == 1:
        delete_line(10)
        output = add_notif()
    elif choice == 2:
        delete_line(10)
        output = update_notif()
    elif choice == 3:
        delete_line(10)
        output = delete_notif()
    else:
        print("Please choose a valid option.")
        reset(100)
        return menu_notif()

    if output == "previous":
        delete_line(100)
        return menu_notif()