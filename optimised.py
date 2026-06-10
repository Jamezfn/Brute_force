#!/usr/bin/env python

from typing import List

def jump(nums: List[int]) -> int:
    res = 0
    l = r = 0

    while r < len(nums) - 1:
        far = 0

        for i in range(l, r + 1):
            far = max(far, i + nums[i])
        l = r + 1
        r = far

        res += 1

    return res

print(jump([2,3,1,1,4]))
