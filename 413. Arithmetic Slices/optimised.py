#!/usr/bin/env python

from typing import List

def numberOfArithmeticSlices(nums: List[int]) -> int:
    """Number of arithmetic arrays"""
    n = len(nums)
    if n < 3:
        return 0

    cur = 0
    total = 0

    for i in range(2, n):
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            cur += 1
            total += cur
        else:
            cur = 0

    return total


print(numberOfArithmeticSlices([1,2,3,4]))
print(numberOfArithmeticSlices([1,3,5,7,9]))
print(numberOfArithmeticSlices([1]))
