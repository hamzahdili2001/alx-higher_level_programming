#!/usr/bin/python3
def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None
