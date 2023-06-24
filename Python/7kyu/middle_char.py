import math

def get_middle(s):
    middle = math.ceil(len(s) / 2) - 1
    if len(s) % 2 > 0:
        print(s[middle])
    else:
        print(s[middle] + s[middle + 1])
