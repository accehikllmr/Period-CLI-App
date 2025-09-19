from modules.mod_formatted_data import formatted_data
from modules.mod_interval import *

def check_notif_day(sendDay):
    '''
    Checks whether notifications are set for dates between most recent and next periods

    Arguments
    ----------
    sendDay (int) : number of days prior to next periods that user wants to receive a notification

    Returns
    --------
    True (bool) : if notification days are within given range
    False (bool) : if notifications days are outside of given range
    '''

    if 0 < sendDay <= interval(formatted_data())[2]:   #third item in list, see interval function returns in mod_interval
        return True
    return False

#MODIFY ACCORDING TO NEW MODULES