#!/usr/bin/python3
"""Module for pascal_triangle"""


def binomial_c(n, k):
    """Calculates binomial coefficient"""
    if (k > n - k):
        k = n - k
    result = 1
    for i in range(k):
        result = result * (n - i)
        result = result // (i + 1)
    return (result)


def pascal_triangle(n):
    """Prints pascal's triangle"""
    triangle_list = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(binomial_c(i, j))
        triangle_list.append(row)
    return triangle_list
