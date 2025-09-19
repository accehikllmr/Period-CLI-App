def check_short(date):
    '''
    Checks input date to see if year is of the correct length

    Arguments
    ----------
    date (str) : date input by user DD/MM/YYYY

    Returns
    --------
    True (bool) : if not enough digits in the input year
    False (bool) : if the correct number of digits in the input year
    '''

    date = date

    if len(date) == 6:
        year = ""
        output = "No year (" + str(year) + ") was entered. "
    elif len(date) == 7:
        year = date[6]
        output = "The year (" + str(year) + ") entered is too far in the past. "
    elif len(date) == 8:
        year = date[6:8]
        output = "The year (" + str(year) + ") entered is in the incorrect format. "
    elif len(date) == 9:
        year = date[6:9]
        output = "The year (" + str(year) + ") entered is too far in the past. "
    elif len(date) > 10:
        year = date[6:]
        output = "The year (" + str(year) + ") entered is in the future. "
    else:
        year = date[6:10]   #need exactly four digits in year for datetime conversions to work
        return False
    return True, output