from modules.mod_input_data import input_data
from modules.mod_reset import reset
from modules.mod_add_contact import add_contact
from modules.mod_update_contact import update_contact
from modules.mod_delete_contact import delete_contact
from modules.mod_delete_line import delete_line
from modules.mod_read_notifications import read_notifications
from modules.mod_add_notif import add_notif
from modules.mod_read_contact import read_contact
from modules.mod_check_enter import check_enter
from modules.mod_check_escape import check_escape

def menu_contact():
    '''
    Shows user the menu for contact information

    Returns
    --------
    menu_contact (function) : calls itself when a valid option is not given by user or when user chooses this option
    output (string) : assigns string to allow escape to previous menu level (settings)
    add_notif (function) : goes to add notification flow if user chooses this option
    '''

    print("***Contact information*** \n 1: Add \n 2: Update \n 3: Delete \nChoose one of the options above.")
    choice = input_data("numbers")

    if check_enter(choice, 100):
        return menu_contact()
    elif check_escape(choice):
        output = check_escape(choice)[1]
        return output

    choice = int(choice)

    if choice == 1:
        delete_line(10)
        output = add_contact()
    elif choice == 2:
        delete_line(10)
        output = update_contact()
    elif choice == 3:
        delete_line(10)
        output = delete_contact()
    else:
        print("Please choose a valid option.")
        reset(100)
        return menu_contact()

    if output == "previous":
        delete_line(100)
        return menu_contact()

    choice = ""

    #control structure to send user to add notifications flow after having completed contact information (SHOULD BE IN add_contact() right?)

    notifInfo = read_notifications()
    contactInfo = read_contact()
    if len(notifInfo[0]) == 0 and len(contactInfo[0]) != 0:
        reset(100)
        while choice != 1 and choice != 0:
            print("You have not yet setup your notifications. Would you like to setup your notifications now? 1 = Yes, 0 = No")
            choice = input_data("numbers")
            if choice == 1:
                return add_notif()
            elif choice == 0:
                return menu_contact()
            else:
                print("Please choose a valid option.")
                delete_line(100)