def check_escape(data):
    '''
    Checks input data to see if escape key was pressed during input

    Arguments
    ----------
    data (str) : data input by user

    Returns
    --------
    True (bool) : if input date contains escape key
    '''

    if data == "escape":
        output = "previous"
        return True, output