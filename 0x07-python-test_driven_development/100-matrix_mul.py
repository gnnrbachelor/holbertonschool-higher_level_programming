#!/usr/bin/python3
"""Multiplies Matrix """


def matrix_mul(m_a, m_b):
    """Matrix Multiply"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_a should contain only integers or floats")

    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_b should contain only integers or floats")

    result = [[0 for a in m_b[0]] for b in m_a]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
