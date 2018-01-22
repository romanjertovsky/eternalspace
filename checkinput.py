import re
#  from output import msg_out

def get_login( msg='Input: ', min_len=1, max_len=20):
    pattern = r"^[A-Za-z0-9-]*$"
    while True:
        txt = input(msg)
        if len(txt) < min_len or len(txt) > max_len:
            print("Minimum {0} characters and maximum {1}, please.".format(min_len, max_len))
            continue
        if re.match(pattern, txt):
            return txt
        else:
            print('Letters, numbers or dashes only, please.')


def get_cmd(msg='Input: ', min_len=1, max_len=20):
    pattern = r"^[a-z0-9-: ]*$"
    while True:
        txt = input(msg)
        if len(txt) < min_len or len(txt) > max_len:
            print("Minimum {0} characters and maximum {1}, please.".format(min_len, max_len))
            continue
        if re.match(pattern, txt):
            return txt
        else:
            print('Letters, numbers, spaces, colons or dashes only, please.')


