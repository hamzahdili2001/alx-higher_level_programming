#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    w_sum = sum(score * weight for score, weight in my_list)
    total = sum(weight for _, weight in my_list)
    return w_sum / total
