#!/usr/bin/python3
"""create a class called myList that inherits from list"""


class MyList(list):
    """inherits from list and implements a new method called print_sorted"""
    def print_sorted(self):
        """prints the list in a ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)


# my_list = MyList([2, 4, 5, 6, 1, -3])

# print(my_list)
# my_list.print_sorted()
