#!/usr/bin/env python

def divide(dividend: int, divisor: int) -> int:
    """"""
    negative = (dividend < 0) != (divisor < 0)
    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0
    while dividend >= divisor:
        temp = divisor
        multiple = 1
        while (temp << 1) <= dividend:
            temp <<= 1
            multiple <<= 1
        dividend -= temp
        quotient += multiple
    if negative:
        quotient = -quotient

    return min(max(-2**31, quotient), 2**31 - 1)

print(divide(-10, -2))
print(divide(7, -3))
print(divide(-15, 4))
