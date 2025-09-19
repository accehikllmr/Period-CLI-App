import msvcrt
import time
from modules.mod_delete_line import delete_line
from modules.mod_stupid_key import stupid_key

def reset(lines):
    '''
    Reads user input to initiate terminal reset

    Arguments
    ----------
    lines (int) : indicates number of lines to erase from screen when resetting terminal

    Returns
    --------
    delete_line() (function) : function call upon input of either escape or enter key
    reset() (function) : restarts itself if any other key is pressed
    '''

    key = ""

    while key != '\x1b' or key != '\x0d':
        key = msvcrt.getch()
        if not stupid_key(key):
            key = key.decode("utf-8")
            if key == "\x1b" or key == "\x0d":  #if input is escape or enter key
                return delete_line(lines)
            else:
                return reset(lines)