#!/usr/bin/env python

from typing import List

def findMaxAverage(nums: List[int], k: int) -> float:
    n = len(nums)
    window_sum = sum(nums[:k])
    res = window_sum
    for i in range(k, n):
        window_sum += nums[i] - nums[i - k]
        res = max(res, window_sum)

    return res / k

print(findMaxAverage([1,12,-5,-6,50,3], 4))
