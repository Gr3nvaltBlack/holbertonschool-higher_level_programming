#!/usr/bin/python3

def pow(a, b):
    result = 1
    while b != 0:
        if b < 0:
            result *= (1 / a)
            b += 1
        else:
            result *= a
            b -= 1
    return result
