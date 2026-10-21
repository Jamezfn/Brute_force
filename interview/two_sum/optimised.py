#!/usr/bin/env python

from typing import List

def two_sum(nums: List[int], target: int) -> bool:
    left, right = 0, len(nums) - 1
    while left < right:
        tt = nums[left] + nums[right]
        if tt == target:
            return true

        if tt < target:
            left += 1
        else:
            right -=1

    return False

print(two_sum([1,3,4,6,8,10,13], 6))
