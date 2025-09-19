def write_settings(day, time):
    '''
    Writes notification setting into text document

    Arguments
    ----------
    day (str) : days prior to next periods when user want to receive notifications
    time (str) : time at which user wants to receive notifications for next periods
    '''

    with open('notifications.txt', 'w') as notifications:   #open file to write, 'w' erases the file prior to writing
        notifications.write(day)
        notifications.write("\n" + time)
        notifications.close()