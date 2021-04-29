#!/usr/bin/python3
def roman_to_int(roman_string):
    dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    sum = 0
    prev = 0
    if (not isinstance(roman_string, str) or roman_string is None):
        return (0)
    for i in range(len(roman_string)):
        if dict.get(roman_string[i], 0) == 0:
            return (0)

        current = dict.get(roman_string[i])

        if current > prev:
            sum += current - 2 * prev
        else:
            sum += current

        prev += current

    return (sum)
