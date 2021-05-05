#!/usr/bin/python3
"""5-text_indentation module. Adds 2 lines after . ? and :"""


def text_indentation(text):
    """ Adds two lines after special characters"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    string = ""
    spec_char =['.', '?', ':']
    for i in text:
        string += i
        if i in spec_char:
            string += "\n\n"
    print(string, end="")
