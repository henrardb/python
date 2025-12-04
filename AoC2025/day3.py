#!/usr/bin/env python3
joltage = 0
with open('day3.txt', 'r') as file:
    for line in file:
        bank = line.rstrip()
        max_dozen = bank[0]
        max_unit = bank[1]

        for i in range(len(bank) - 2):
            if bank[i+2] > max_unit:
                max_unit = bank[i+2]
            if bank[i+1] > max_dozen:
                max_dozen = bank[i+1]
                max_unit = bank[i+2]

        print(max_dozen + max_unit)
        joltage += int(max_dozen + max_unit)
print(joltage)