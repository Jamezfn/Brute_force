#!/usr/bin/env python

from typing import List

def findMaxAverage(nums: List[int], k: int) -> float:
    n = len(nums)
    res = float("-inf")
    for i in range(n - k + 1):
        sm = 0
        for j in range(i, i + k):
            sm += nums[j]
        res = max(res, sm / k)

    return res

print(findMaxAverage([1,12,-5,-6,50,3], 4))
