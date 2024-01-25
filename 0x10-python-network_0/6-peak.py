#!/usr/bin/python3
def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers."""
    if not len(list_of_integers):
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 2:
        if list_of_integers[0] > list_of_integers[1]:
            return list_of_integers[0]
        else:
            return list_of_integers[1]
    else:
        if len(list_of_integers) % 2:
            mid = len(list_of_integers) // 2
        else:
            mid = (len(list_of_integers) // 2) - 1

        if len(list_of_integers) % 2:
            if (
                list_of_integers[mid - 1]
                < list_of_integers[mid]
                > list_of_integers[mid + 1]
            ):
                return list_of_integers[mid]
            else:
                if (
                    list_of_integers[mid - 1]
                    > list_of_integers[mid + 1]
                ):
                    return find_peak(list_of_integers[:mid])
                else:
                    return find_peak(list_of_integers[mid + 1:])
        else:
            if list_of_integers[mid] >= list_of_integers[mid + 1]:
                return find_peak(list_of_integers[:mid + 1])
            else:
                return find_peak(list_of_integers[mid + 1:])
