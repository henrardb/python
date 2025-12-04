#!/usr/bin/env python3
joltage = 0
with open('day3.txt', 'r') as file:
    for line in file:
        bank = line.rstrip()
        to_remove = len(bank) - 12
        result = []

        for digit in bank:
            while to_remove > 0 and result and result[-1] < digit:
                result.pop()
                to_remove -= 1

            result.append(digit)

        if to_remove > 0:
            result = result[:-to_remove]

        print("".join(result))
        joltage += int("".join(result))

print(joltage)