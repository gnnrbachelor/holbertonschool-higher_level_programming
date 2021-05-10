#!/usr/bin/python3
"""Multiplies Matrix """


def matrix_mul(m_a, m_b):
    """Matrix Multiply"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    row_len_a = len(m_a[0])
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
        if len(i) == 0:
            raise ValueError("m_a can't be empty")
        if len(i) != row_len_a:
            raise TypeError("each row of m_a must be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_a should contain only integers or floats")

    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    row_len_b = len(m_b[0])
    for i in m_b:
        row_len_b = len(i)
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")
        if row_len_b == 0:
            raise ValueError("m_a can't be empty")
        if len(i) != row_len_b:
            raise TypeError("each row of m_b must be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_b should contain only integers or floats")

    result = [[0 for a in m_b[0]] for b in m_a]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
