#!/usr/bin/python3

def uniq_add(my_list=[]):
    result_list = 0
    for idx in set(my_list):
        result_list += idx
    return result_list
