#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    List = my_list
    if idx < 0 or idx >= len(my_list):
        return List
    else:
        List[idx] = element
        return List
