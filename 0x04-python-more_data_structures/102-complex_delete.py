#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    deletion = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            deletion.append(key)

    [a_dictionary.pop(key) for key in deletion]
    return a_dictionary

