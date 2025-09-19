from datetime import datetime
from modules.mod_formatted_data import *

def interval(formatted_dates):
    '''
    Calculates the average interval between periods, the date of the next period and days until that date

    Arguments
    ----------
    formatted_dates (lst) : list of dates formatted using datetime module in order to allow math operations

    Returns
    --------
    interval (int) : calendar interval (not including hours, minutes, etc.) of time between this date and the date of the next period
    next_date (str) : date of the next period
    '''

    average_interval = (formatted_dates[-1] - formatted_dates[0])/(len(formatted_dates)-1)  #interval between first and last date divided by total time in between

    next_date = formatted_dates[-1] + average_interval  #determine next period date (including hours, minutes, etc.) by adding result from previous line to last period
    next_date = next_date.replace(hour=0, minute=0, second=0, microsecond=0)    #truncating hours, minutes, etc. in order to calculate calendar interval, not exact time

    today = datetime.today()    #current date, including hours, minutes, etc.
    today = today.replace(hour=0, minute=0, second=0, microsecond=0)
    
    interval = next_date - today    #interval between now and next period date
    interval = interval.days    #keeping only days attribute from object

    next_date = datetime.strftime(next_date, '%d %m %Y')    #convert datetime object to string format, in DD/MMM/YYYY
    average_interval = average_interval.days

    return interval, next_date, average_interval #comma creates tuple date type