def check_month(date):
    '''
    Checks input date to see if month is valid

    Arguments
    ----------
    date (str) : date input by user DD/MM/YYYY

    Returns
    --------
    True (bool) : if input month is a valid month
    i (list) : list with month and maximum number for day
    '''

    months = [["01", 31], ["02", 28], ["03", 31], ["04", 30], ["05", 31], ["06", 30], ["07", 31], ["08", 31], ["09", 30], ["10", 31], ["11", 30], ["12", 31]]
    for i in months:
        if i[0] == date[3:5]:   #to harmonize writing of months with those in above list, check if input month appears in list
            return True, i