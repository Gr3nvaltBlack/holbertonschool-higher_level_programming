#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None
    max_Val = my_list[0]
    for idx in my_list:
        if idx > max_Val:
            max_Val = idx
    return max_Val
