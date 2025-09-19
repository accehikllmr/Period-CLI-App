def check_early(date):
    '''
    Checks input year to see if above arbitrary boundary

    Arguments
    ----------
    date (str) : date input by user DD/MM/YYYY

    Returns
    --------
    True (bool) : if input year is above arbitrary boundary
    '''

    if 1900 > int(date[6:10]): #unbound date to include all digits
        return True