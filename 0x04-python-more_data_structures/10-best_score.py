#!/usr/bin/python3
def best_score(my_dict):
    winner = ""
    high = -1

    if my_dict is None:
        return
    for key in my_dict:
        if high == 0:
            high = my_dict[key]
            winner = key
        if (my_dict[key] > high):
            high = my_dict[key]
            winner = key
    if high == -1:
        return None
    return winner
