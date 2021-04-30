#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        divisor = 0
        dividend = 0
        for i in my_list:
            dividend += i[0] * i[1]
            divisor += i[1]
        return (dividend / divisor)
