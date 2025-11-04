#!/usr/bin/env python3
import math


def best_tax_calculation(tax: float) -> float:
    return (100 * (math.log(tax+1) - (tax-0.2)**2 + 0.04))


def derivative(tax: float) -> float:
    return (100 * (1/(tax+1) - 2*(tax-0.2)))


if __name__ == "__main__":
    actual_rate: float = 0.7
    threshold: float = 0.0001
    step: float = 0.001
    iteration: int = 0
    max_iteration: int = 100000
    follow: bool = True

    while follow:
        rate_variation = step * derivative(actual_rate)
        actual_rate = actual_rate + rate_variation

        if abs(rate_variation) < threshold:
            print(actual_rate)
            follow = False

        if iteration > max_iteration:
            follow = False

        iteration += iteration
