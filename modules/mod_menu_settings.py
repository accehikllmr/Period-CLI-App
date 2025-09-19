import sys
import msvcrt
from datetime import datetime
from modules.mod_read_notifications import read_notifications
from modules.mod_check_notif_day import check_notif_day
from modules.mod_check_notif_time import check_notif_time
from modules.mod_write_settings import write_settings
from modules.mod_read_contact import read_contact
from modules.mod_reset import reset
from modules.mod_delete_line import delete_line
from modules.mod_input_data import input_data
from modules.mod_menu_contact import menu_contact
from modules.mod_menu_notif import menu_notif
from modules.mod_check_enter import check_enter
from modules.mod_check_escape import check_escape

def menu_settings():
    '''
    Shows user menu for application settings

    Returns
    --------
    menu_setting (function) : calls itself when a valid option is not given by user or when user chooses this option
    output (string) : assigns string to allow escape to previous menu level (settings)
    '''   
    
    output = ""

    print("***Settings*** \n 1: Contact information \n 2: Notifications \nChoose one of the options above: ")
    choice = input_data("numbers")

    if check_enter(choice, 100): #split up from other conditional since sending to different menus
        return menu_settings()
    elif check_escape(choice):
        output = check_escape(choice)[1]    #second element of tuple returned by function
        return output

    choice = int(choice)

    if choice == 1:
        delete_line(10)
        output = menu_contact()
    elif choice == 2:
        delete_line(10)
        output = menu_notif()
    else:
        print("Please choose a valid option.")
        reset(100)
        return menu_settings()

    if output == "previous":    #sends user back to previous menu if escape is returned from above function calls
        delete_line(100)
        return menu_settings()

    #current_settings = read_contact()
    
    #for i in current_settings:
     #   if len(i) == 0:
      #      set_contact()

    #output = ""
    #fail = "Your notification settings have not been updated."

    #sendDay = ""
    #while not sendDay.isdigit():    #to force the entry of digits, since int data type needed for checking validity of day
     #   sendDay = input("How many days prior to your periods would you like to receive notifications? ") #day of notification
      #  if not sendDay.isdigit():
       #     delete_line(1)  #delete line so that it can be overwritten by new input
#    sendDay = int(sendDay)  #convert to integer for checking validity in following lines
#
 #   if check_notif_day(sendDay):
  #      sendTime = input("At what time of the day (HH:MM) would you like to receive these notifications? ") #time of day of notification
   #     if check_notif_time(sendTime):
    #        output = "Your notifications will be sent " + str(sendDay) + " days before your next periods at " + sendTime + "."
     #       write_settings(str(sendDay), sendTime)  #call function to overwrite existing setting only if data is valid
      #  else:
       #     output = "The time entered must have hours from 0 to 23, minutes from 0 to 59 and be separated by a colon. " + fail
    #elif sendDay < 1:  #not permitting entries on day of or after periods
     #   output = "Notifications for periods must occur prior to the day of the next period. " + fail
    #else:   #not permitting outside of average interval of periods
     #   output = "Notifications for periods must occur after the most recent period. " + fail

    #return output

#find way to have app check every day

#sendTime = datetime.strptime(sendTime, "%H:%M").time() -> for later, when needing to interpret string as actual time