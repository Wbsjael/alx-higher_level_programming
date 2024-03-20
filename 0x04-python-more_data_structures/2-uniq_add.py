#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = []
    for j in my_list:
        if j not in uniq_list:
            uniq_list.append(j)
    res = sum(uniq_list)
    return res
