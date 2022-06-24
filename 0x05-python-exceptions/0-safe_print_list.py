#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in x:
            print("{}".format(my_list[i]))
    except IndexError:
        print("index out of bound")
