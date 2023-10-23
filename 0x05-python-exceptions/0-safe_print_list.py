#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    y = 0
    try:
        my_list[x]
        for i in range(x):
            print(my_list[i], end='')
            y += 1
    except IndexError:
        for i in my_list:
            print(i, end='')
            y += 1
    print()
    return (y)
