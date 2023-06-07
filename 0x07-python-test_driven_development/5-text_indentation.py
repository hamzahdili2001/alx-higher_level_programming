#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in [".", "?", ":"]:
        text = text.replace(char, char + "\n\n")

    lines = [line.strip() for line in text.split("\n")]

    print("\n".join(lines))
