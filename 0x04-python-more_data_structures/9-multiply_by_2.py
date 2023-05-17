#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}
    for key, val in a_dictionary.items():
        new_dic[key] = val * 2
    return new_dic
