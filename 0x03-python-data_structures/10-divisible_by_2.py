#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    truth_arr = []
    if my_list:
        for i in my_list:
            if i % 2 == 0:
                truth_arr.append(True)
            else:
                truth_arr.append(False)
    return (truth_arr)
