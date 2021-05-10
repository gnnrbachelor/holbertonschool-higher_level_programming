#!/usr/bin/python3
"""Multiplies Matrix """


def matrix_mul(m_a, m_b):
    """Matrix Multiply"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")

    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    row_len_a = len(m_a[0])
    for i in m_a:
        if len(i) == 0:
            raise ValueError("m_a can't be empty")
        if len(i) != row_len_a:
            raise TypeError("each row of m_a must be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_a should contain only integers or floats")

    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    row_len_b = len(m_b[0])
    for i in m_b:
        if len(i) == 0:
            raise ValueError("m_b can't be empty")
        if len(i) != row_len_b:
            raise TypeError("each row of m_b must be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_b should contain only integers or floats")

    if row_len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for a in m_b[0]] for b in m_a]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
