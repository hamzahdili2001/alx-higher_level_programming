#!/usr/bin/python3
def best_score(a_dictionary):
    df = None
    if a_dictionary is None:
        return df
    score = max(a_dictionary.values(), default=df)
    for key, val in a_dictionary.items():
        if score == val:
            return key
