#!/usr/bin/python3
"""Json"""


def class_to_json(obj):
    """a function that returns the dictionary
    description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object:"""
    j_dict = {}
    if hasattr(obj, "__dict__"):
        for k, v in obj.__dict__.items():
            if isinstance(v, (list, str, bool, int, dict)):
                j_dict[k] = v
    return j_dict
