#!/usr/bin/env python3
import math


def dich_search(to_find: int, sorted_list: list[int]) -> int:
    minimum: int = 0
    maximum: int = len(sorted_list)
    to_compare: int = math.floor(len(sorted_list)/2)

    while abs(sorted_list[to_compare] - to_find) > 0.0001:
        if to_find < sorted_list[to_compare]:
            maximum = to_compare
            to_compare = math.floor((to_compare + minimum)/2)
        if to_find > sorted_list[to_compare]:
            minimum = to_compare
            to_compare = math.floor((to_compare + maximum)/2)
    return to_compare


if __name__ == "__main__":
    to_find = 45
    sorted_list = [2, 5, 7, 9, 12, 15, 33, 45, 55, 67, 78, 89, 100]
    print(dich_search(to_find, sorted_list))
