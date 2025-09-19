from modules.mod_input_data import input_data
from modules.mod_check_future import check_future
from modules.mod_check_short import check_short
from modules.mod_check_slash import check_slash
from modules.mod_check_month import check_month
from modules.mod_check_day import check_day
from modules.mod_check_early import check_early
from modules.mod_check_leap import check_leap

def add_date():
    '''
    Appends new date into the period date text file

    Returns:
    --------
    output (str) : success or failure message personnalized according to the user input, or string needed to trigger desired action elsewhere
    '''
    
    print("***1: Record Period Start Date*** \nWhen did your period start? (DD/MM/YYYY) ")
    date = input_data("date")

    with open('classified_data.txt', 'a') as dates: #opens data file for appending only
        fail = "The date has not been added."   #output messages according to be added based on user input
        success = "\nThe date has been added."    #next line added due to stranger overwrite printing error
        output = ""
        
        if date == "enter": #modified module to fit other use cases, but boolean condition is simple enough
            dates.close()
            output = "No date has been added."
            return output   #exit immediately, to avoid data type and range errors in following tests
        elif date == "escape":
            dates.close()
            output = "previous"
            return output
        elif check_slash(date):
            output = "\nOne or both of the slashes is not in the correct position. " + fail
            dates.close()
            return output
        elif check_short(date): #old name, checks year now, not length
            output = check_short(date)[1] + fail
            dates.close()
            return output
        elif check_month(date):
            mmdd = check_month(date)[1]
            month = mmdd[0]
            day = mmdd[1]
            if check_day(day, date):
                if check_future(date)[0] < check_future(date)[1]:    #if date is after today, do not accept data
                    output = "\nThe date entered is in the future. " + fail
                elif check_early(date):   #comparing input year with arbitrary lower bound
                    output = "\nThe year entered (" + date[6:10] + ") is not after 1900. " + fail  #added year to highlight error to user
                else:
                    output = success    #passed all checks
                    dates.write("\n" + date)
            elif check_leap(day, month, date):
                if check_future(date)[0] < check_future(date)[1]:    #if date is after today, do not accept data
                    output = "\nThe date entered is in the future. " + fail
                elif check_early(date):
                    output = "\nThe year entered (" + date[6:10] + ") is not after 1900. " + fail
                else:
                    output = success
                    dates.write("\n" + date)
            else:
                output = "\nThe day entered (" + date[0:2] +") is too large for the given month. " + fail
        else:
            output = "\nThe month entered (" + date[3:5] + ") does not correspond to one of the twelve months in the year. " + fail
        
        dates.close()
        return output