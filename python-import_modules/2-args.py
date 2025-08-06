#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    nb_args = len(argv) - 1
    if nb_args == 0:
        print("{} arguments.".format(nb_args))
    elif nb_args == 1:
        print("{} argument:".format(nb_args))
    else:
        print("{} arguments:".format(nb_args))
    for i in range(nb_args):
        print("{}: {}".format(i + 1, argv[i + 1]))
