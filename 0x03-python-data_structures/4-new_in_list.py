#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        new_list = my_list
        return new_list
    else:
        for i in range(0, my_list):
            if i == idx:
                my_list[i] = element
        return my_list
