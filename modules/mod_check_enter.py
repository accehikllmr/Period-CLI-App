from modules.mod_reset import reset

def check_enter(data, lines):
    '''
    Checks input data to see if enter key was pressed during input

    Arguments
    ----------
    data (str) : data input by user

    Returns
    --------
    True (bool) : if input date contains enter key
    '''

    if data == "enter":
        print("Please choose a valid option.")
        reset(lines)
        return True