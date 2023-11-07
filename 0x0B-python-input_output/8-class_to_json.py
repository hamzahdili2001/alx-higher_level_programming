#!/usr/bin/python3
"""8-class_to_json.py"""


def class_to_json(obj):
    """
    function that returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean) for
    JSON serialization of an object
    """

    attrs = obj.__dict__

    json = {}

    for key, value in attrs.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json[key] = value

    return json
