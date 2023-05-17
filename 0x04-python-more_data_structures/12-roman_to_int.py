#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_to_int_dict = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    result = 0
    last = 0

    for c in roman_string:
        if c in roman_to_int_dict:
            value = roman_to_int_dict[c]
            if last == 0 or last >= value:
                result += value
            elif last < value:
                result += value - (last * 2)
            last = value
    return int(result)
