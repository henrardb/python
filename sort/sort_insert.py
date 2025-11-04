#!/usr/bin/env python3

def insert(number: int, sorted_list: list[int]) -> list[int]:
    position = len(sorted_list) - 1
    
    while position >= 0 and number < sorted_list[position]:
        position -= 1

    sorted_list.insert(position + 1, number)
    return sorted_list 

def sort_insert(not_sorted_list: list[int]) -> list[int]:
    new_list = []
    while len(not_sorted_list) != 0:
        insert(not_sorted_list.pop(0), new_list)

    return new_list

if __name__ == "__main__" :
    not_sorted_list = [8,4,6,1,2,5,3,7]
    print(sort_insert(not_sorted_list))
