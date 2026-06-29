#!/usr/bin/env python

def mySqrt(x: int) -> int:
    i, j = 0, x
    while i <= j:
        mid = (i + j) // 2
        square = mid * mid

        if square == x:
            return mid
        elif square < x:
            i = mid + 1
        else:
            j = mid - 1

    return j

print(mySqrt(8))
