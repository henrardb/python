#!/usr/bin/env python3
def pgcd(a, b):
    big = max(a, b)
    small = min(a, b)

    rest = big % small

    if rest == 0:
        return small
    else:
        return pgcd(small, rest)


print(pgcd(105, 33))
