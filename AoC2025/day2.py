#!/usr/bin/env python3
ranges = "2200670-2267527,265-409,38866-50720,7697424-7724736,33303664-33374980,687053-834889,953123-983345,3691832-3890175,26544-37124,7219840722-7219900143,7575626241-7575840141,1-18,1995-2479,101904-163230,97916763-98009247,52011-79060,31-49,4578-6831,3310890-3365637,414256-608125,552-1005,16995-24728,6985-10895,878311-912296,59-93,9978301-10012088,17302200-17437063,1786628373-1786840083,6955834840-6955903320,983351-1034902,842824238-842861540,14027173-14217812"
#ranges = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
code = 0


def is_invalid(num):
    number_to_string = str(num)
    size = len(number_to_string)

    for l in range(1, size // 2 + 1):
        if size % l == 0:
            pattern = number_to_string[0:l]
            r = size // l
            repeated_string = pattern * r

            if repeated_string == number_to_string:
                return True

    return False


for range_number in ranges.split(','):
    print("\nRange_number\n-----------")
    range_content = range_number.split('-')

    for number in range(int(range_content[0]), int(range_content[1]) + 1):
        if is_invalid(number):
            code += number

print(code)