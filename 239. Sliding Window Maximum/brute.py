#!/usr/bin/env python

from typing import List

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    w = []

    for i in range(n - k + 1):
        max_val = nums[i]
        for j in range(i, k + i):
            if nums[j] > nums[i]:
                max_val = nums[j]
        w.append(max_val)
    
    return w


print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(maxSlidingWindow([1], 1))
