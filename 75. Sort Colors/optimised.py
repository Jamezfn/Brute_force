#!/usr/bin/env python

from typing import List

def sortColors(nums: List[int]) -> None:
    count = [0, 0, 0]

    for num in nums:
        count[num] += 1

    i = 0

    for c in range(3):
        while count[c] > 0:
            nums[i] = c
            i += 1
            count[c] -= 1

nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)
