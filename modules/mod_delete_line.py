import sys

def delete_line(lines):
    '''
    Reset the terminal by deleting the printed information

    Arguments
    ----------
    lines (int) : number of lines to be erased from user interface in order to reset command line interface (UI)
    '''

    for i in range(lines): #lines defined according to need in call
        sys.stdout.write("\x1b[1A")    #moves cursor up one line
        sys.stdout.write("\x1b[2K")    #erases the line where the cursor is positioned

    for i in range(lines):  #deletes upwards, which rids of stray keys from input_data
        sys.stdout.write("\x1b[1B")
        sys.stdout.write("\x1b[2K")

    for i in range(lines):  #resets cursor to top of screen, for next output to user
        sys.stdout.write("\x1b[1A")