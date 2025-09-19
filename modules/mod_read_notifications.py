def read_notifications():
    '''
    Reads interval of time to send notifications

    Returns
    --------
    sendWhen (int) : number of days prior to periods to send notifications
    '''

    with open('notifications.txt', 'r') as notifications:   #open to read if notifications have already been set
        sendWhen = ""
        sendThen = ""
        current_settings = notifications.readlines()
        if len(current_settings) > 0:
            sendWhen = current_settings[0]  #extract existing data before erasing it
            sendThen = current_settings[1]
        notifications.close()
    return sendWhen, sendThen
