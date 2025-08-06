#!/usr/bin/python3

def multiple_returns(sentence):
    idx = len(sentence)
    if idx == 0:
        Char = None
    else:
         Char = sentence[0]
    tuple_val = (idx, sentence[0])
    return tuple_val
