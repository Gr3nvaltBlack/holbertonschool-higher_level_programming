#!/usr/bin/python3

count = 0
    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end="")
            count += 1
        except (TypeError, ValueError):
            continue
    print()
    return count
