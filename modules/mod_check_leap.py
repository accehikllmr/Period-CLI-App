from modules.mod_check_day import check_day

def check_leap(day, month, date):
    '''
    Checks input date to see if during leap year

    Arguments
    ----------
    day (int) : day (DD) input by user
    month (str) : month (MM) input by user
    date (str) : date input by user DD/MM/YYYY

    Returns
    --------
    True (bool) : if input day is within month range, including february in leap year
    '''

    year = int(date[6:])
    
    case_one = year % 4 == 0 and year % 100 != 0
    case_two = year % 400 == 0
    cases = case_one or case_two
    
    if month == "02" and cases:    #extra cases for leap years
        day = day + 1
        if check_day(day, date):
            return True
    return False