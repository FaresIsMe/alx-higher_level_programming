#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    my_list.pop(idx)
    my_list.insert(idx, element)
    return my_list
