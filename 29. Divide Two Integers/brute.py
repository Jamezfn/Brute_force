#!/usr/bin/env python

def divide(dividend: int, divisor: int) -> int:
    """"""
    sign = (dividend < 0) != (divisor < 0)
    dividend = abs(dividend)
    divisor = abs(divisor)

    count = 0
    while dividend >= divisor:
        dividend -= divisor
        count += 1

    if sign:
        count = -count
    return min(max(-2**31, count), 2**31 - 1)

print(divide(-10, -2))
print(divide(7, -3))
print(divide(-15, 4))
