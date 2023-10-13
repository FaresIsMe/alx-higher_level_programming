#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dir = a_dictionary
    for i in new_dir:
        new_dir[i] = new_dir[str(i)] * 2
    return new_dir
