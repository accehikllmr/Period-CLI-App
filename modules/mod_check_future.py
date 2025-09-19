from datetime import datetime

def check_future(date):
    '''
    Checks input date is after today (in the future)

    Arguments
    ----------    
    date (str) : date input by user DD/MM/YYYY

    Returns
    --------
    today (datetime) : current date in datetime format, for future calculations
    compare_date (datetime) : input date in datetime format, for future calculations
    '''

    today = datetime.today()    #used to compare with entered date
    today = today.replace(hour=0, minute=0, second=0, microsecond=0)

    date = date

    compare_date = ""   #new string for correctly formatted date
    for i in date:
        if i.isalnum(): #add to new string if not symbol
            compare_date += i
        else:   # replace symbols with spaces
            compare_date += " "
    
    compare_date = datetime.strptime(compare_date, '%d %m %Y')
    compare_date = compare_date.replace(hour=0, minute=0, second=0, microsecond=0)
    
    return today, compare_date  #returns in form of a tuple