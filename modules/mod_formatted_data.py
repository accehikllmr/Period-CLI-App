from datetime import datetime

def formatted_data():
    '''
    Formats dates in datetime format to allow math operations

    Returns
    --------
    formatted_dates (lst) : list of dates formatted in datetime format
    '''

    with open('classified_data.txt') as data_file:
        data = data_file.readlines()[1:] #take all of the data and make a list, omit first line (the title)
        dates = []  #new sets in which to store modified list elements
        formatted_dates = []
        for i in data:
            i = i[0:2] + " " + i[3:5] + " " + i[6:10]   #keeping information, removing symbols and adding spaces before converting into datetime format
            dates.append(i)
        for i in dates:
            i = datetime.strptime(i, '%d %m %Y')    #convert string format into datetime format (needed for interval calculations)
            formatted_dates.append(i)
        data_file.close()
    return formatted_dates