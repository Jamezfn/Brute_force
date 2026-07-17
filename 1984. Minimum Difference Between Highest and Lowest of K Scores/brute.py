#!/usr/bin/env python

from typing import List

def minimumDifference(nums: List[int], k: int) -> int:
    nums.sort()
    res = float('inf')

    for i in range(len(nums) - k + 1):
        res = min(res, (nums[i + k - 1] - nums[i]))

    return res

print(minimumDifference([9,4,1,7], 2))
