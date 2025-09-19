def check_notif_time(sendTime):
    '''
    Checks whether notifications are set for valid times in 24-hour clock

    Arguments
    ----------
    sendTime (str) : time at which user wants to receive notifications on given day

    Returns
    --------
    True (bool) : if time falls within given hour and minute ranges
    False (bool) : if time falls outside of given hour and minute ranges
    '''

    if len(sendTime) == 4 and sendTime[1] == ":" and int(sendTime[2:]) < 60:
        return True
    elif len(sendTime) == 5 and sendTime[2] == ":" and 0 < int(sendTime[0:2]) < 24 and int(sendTime[3:]) < 60:
        return True
    else:
        return False

#MODIFY ACCORDING TO NEW MODULES
