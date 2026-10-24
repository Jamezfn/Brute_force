#!/usr/bin/env python

from typing import List

def moveZeroes(nums: List[int]) -> None:
    i = 0

    for j in range(len(nums)):
        if (nums[j] != 0):
            nums[j], nums[i] = nums[i], nums[j]

            i += 1

nums = [2,0,4,0,9]
print(nums)
moveZeroes(nums)
print(nums)
