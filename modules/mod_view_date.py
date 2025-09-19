from datetime import datetime
from modules.mod_interval import interval
from modules.mod_formatted_data import formatted_data

def view_date():
    '''
    Outputs days until the next period and the specific date

    Returns
    --------
    view (str) : output statement giving days until and date of next period
    '''

    print("***2: View Next Period Date***")
    
    days = interval(formatted_data())   #return of function is a tuple, calling function to format dates again (fix for no file found)
    
    view = "Your next period is in " + str(days[0]) + " days on " + str(days[1]) + "."
    return view