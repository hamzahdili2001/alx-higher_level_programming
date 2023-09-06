#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    current_index = 0
    while current_index < len(text) and text[current_index] == ' ':
        current_index += 1

    while current_index < len(text):
        print(text[current_index], end="")

        if text[current_index] == "\n" or text[current_index] in ".?:":
            if text[current_index] in ".?:":
                print("\n")

            current_index += 1

            while current_index < len(text) and text[current_index] == ' ':
                current_index += 1

            continue

        current_index += 1
