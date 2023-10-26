#!/usr/bin/python3
'''
Function that formated string
Usage:
    say_my_name(first_name, last_name)
'''


def say_my_name(first_name, last_name=""):
    '''
    Function that prints My name is <first name> <last name>
    Prints: My name is <first name> <last name>'''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    say_name = "My name is {} {}".format(first_name, last_name)
    print(say_name)
