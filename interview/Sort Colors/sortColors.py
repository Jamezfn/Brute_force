#!/usr/bin/env python

from typing import List

def sortColors(nums: List[int]) -> None:
    l = 0
    r = len(nums) - 1

    i = 0

    while i <= r:
        if nums[i] == 0:
            nums[i], nums[l] = nums[l], nums[i]
            l += 1

        elif nums[i] == 2:
            nums[i], nums[r] = nums[r], nums[i]
            r -= 1
        else:
            i += 1

nums = [2,1,2,0,1,0,1,0,1]
sortColors(nums)
print(nums)
