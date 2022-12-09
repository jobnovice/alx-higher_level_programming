#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lg = -1(number * -1 % 10)
        return (lg)
    else:
        lg = number % 10
        return(lg)
