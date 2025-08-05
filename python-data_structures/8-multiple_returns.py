#!/usr/bin/python3

def multiple_returns(sentence):
    for idx in range(len(sentence)):
        if sentence == "":
            sentence[0] = None
            return idx, sentence[0]
    return idx, sentence[0]
