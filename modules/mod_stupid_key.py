def stupid_key(key):
    '''
    Checks to see whether a key that cannot be decoded in utf-8 has been pressed

    Returns
    --------
    True (bool) : if either a function key or a cursor control key has been pressed
    False (bool) : if a key that can be decoded in utf-8 has been pressed
    '''

    if key == b'\xe0' or key == b'\x00':
        return True
    return False
