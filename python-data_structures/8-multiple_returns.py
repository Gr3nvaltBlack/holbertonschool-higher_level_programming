#!/usr/bin/python3

def multiple_returns(sentence):
    idx = len(sentence)
    if idx == 0:
        Char = None
    else:
        Char = sentence[0]
    tuple_val = (idx, Char)
    return tuple_val
