#!/usr/bin/env python3

if __name__ == "__main__":
    position = 50
    password = 0
    with open('day1.txt', 'r') as file:
        for line in file:
            amount = int(line[1:])
            direction = line[0]

            if direction == 'L':
                step = -1
            else:
                step = 1

            for _ in range(amount):
                position = (position + step) % 100

                if position == 0:
                    password += 1

    print(password)