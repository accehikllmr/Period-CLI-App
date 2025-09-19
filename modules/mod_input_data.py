import msvcrt   #module for recognizing single keystrokes
import sys
from modules.mod_stupid_key import stupid_key

def input_data(dataType):
    '''
    Allows the user to input the data

    Arguments
    ----------
    dataType (str) : identifies the type of data to be entered by the user and yields desired restrictions

    Returns
    --------
    valid (str) : data input by user, including only relevant characters and keystrokes according to restrictions given by input data
    '''

    key = ""
    valid = ""

    while key != "\x0d": #stop when enter key is pressed
        
        key = msvcrt.getch()    #not using getche since do not want invalid characters to print on screen

        if stupid_key(key):
            continue    #skip loop iteration since invalid character

        key = key.decode("utf-8")   #decode only after ridding of incompatible ANSI codes, prevents errors

        if dataType == "date" and not key.isdigit() and key != "/" and key != "\x0d" and key != "\x1b" and key != "\x08":  #restart loop if one of the valid codes is not pressed
            continue
        elif dataType == "numbers" and not key.isdigit() and key != "\x0d" and key != "\x1b" and key != "\x08": #extra condition for if only want numbers, no slashes
            continue
        
        if key == "\x0d" and valid == "":   #condition when enter is pressed without entering any information (empty string)
            valid = "enter"
            return valid
        elif key == "\x1b": #abort on escape key
            valid = "escape"
            print("") #without it, UI breaks, not sure why exactly, but that was before, no longer
            return valid
        elif key == "\x08" and len(valid) > 0: #when backspace is pressed
            sys.stdout.write('\b \b') #reaplces character with space and moves the cursor back
            sys.stdout.flush() #makes the previous commands show up on the screen
            valid = valid[0:-1] #truncate end of data string
        else:
            sys.stdout.write(key) #print valid characters onto screen
            sys.stdout.flush()
            valid = valid + key #add valid kestrokes to data
    
    valid = valid[0:-1]
    return valid