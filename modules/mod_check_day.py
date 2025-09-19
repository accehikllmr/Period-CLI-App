def check_day(day, date):
    '''
    Checks input day to see if within month range

    Arguments
    ----------
    day (int) : day (DD) input by user
    date (str) : date input by user DD/MM/YYYY

    Returns
    --------
    True (bool) : if input day is within month range
    '''

    if day >= int(date[0:2]) >= 1: #comparing input day with upper limit of days in month, from above list
        return True