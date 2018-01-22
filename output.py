import time


def msg_out(string, color=None, wait=0):
    """
    :param string: text for printing
    :param color:  r - red, b - blue, y - yellow
    :param wait: seconds for sleep after output
    :return: is nothing

    Red - error messages .
    Blue - the story, plot.
    Yellow - x3
    """

    if color == 'r':
        print('\033[31m' + string + '\x1b[0m')
    elif color == 'b':
        print('\033[94m' + string + '\x1b[0m')
    elif color == 'y':
        print('\033[93m' + string + '\x1b[0m')
    else:
        print(string)
    time.sleep(wait)
