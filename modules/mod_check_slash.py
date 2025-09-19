def check_slash(date):
    '''
    Checks input date to see if slashes (/) are well positioned

    Arguments
    ----------
    date (str) : date input by user DD/MM/YYYY

    Returns
    --------
    True (bool) : if at least one slash is not well positioned
    '''

    if len(date) < 6 or date[2] != chr(47) or date[5] != chr(47):    #to prevent users from entering single digits for the day and to avoid math operations on symbols, also checks if length is too short
        return True
    return False