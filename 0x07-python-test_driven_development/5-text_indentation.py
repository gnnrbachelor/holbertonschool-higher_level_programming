#!/usr/bin/python3
"""5-text_indentation module"""


def text_indentation(text):
    """Adds two lines after special characters """
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = False
    for i in text:
        if flag:
            if i == " ":
                continue
            flag = False
        if i == '.' or i == '?' or i == ':':
            print(i)
            print("")
            flag = True
        else:
            print(i, end="")
