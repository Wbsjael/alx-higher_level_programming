#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        scores_sum = sum(score * weight for score, weight in my_list)
        weights_sum = sum(weight for score, weight in my_list)

        average = scores_sum / weights_sum
        return average
