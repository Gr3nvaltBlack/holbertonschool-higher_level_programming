#!/usr/bin/python3

def multiple_returns(sentence):
    idx = len(sentence)
    if idx == 0:
        sentence[0] = None
    tuple_val = (idx, sentence[0])
    return tuple_val
