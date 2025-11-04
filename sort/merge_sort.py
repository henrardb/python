#!/usr/bin/env python3
import math

def merge_sort(list_1: list[int], list_2: list[int]) -> list[int]:
    new_list: list[int] = []

    while min(len(list_1), len(list_2)) > 0: 
        if list_1[0] < list_2[0]:
            new_list.append(list_1.pop(0))
        else:
            new_list.append(list_2.pop(0))

    if len(list_1) == 0:
       for i in list_2:
           new_list.append(i)
    else:
       for i in list_1:
           new_list.append(i)

    return new_list

def tri_fusion(list_1: list[int]):
    new_list: list[int] = []

    if len(list_1) == 1:
        new_list = list_1
    else:
        left = tri_fusion(list_1[:math.floor(len(list_1)/2)])
        right = tri_fusion(list_1[math.floor(len(list_1)/2):])
        new_list = merge_sort(left, right)
        
    return new_list

if __name__ == "__main__":
    list_1 = [20, 4, 7, 8, 8, 8.5, -9,  10, 12, 6, 13, 14]

    print(tri_fusion(list_1))
