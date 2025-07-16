#!/usr/bin/env python

from typing import List

def fourSum(nums: List[int], target: int) -> List[List[int]]:
    """Compute a list of 4 integer list: adding up to target using brute force"""
    n = len(nums)
    res = set()
    for i in range(n-3):
        for j in range(i+1, n-2):
            for k in range(j+1, n-1):
                for l in range(k+1, n):
                    s = nums[i] + nums[j] + nums[k] + nums[l]
                    if s == target:
                        tag = tuple(sorted([nums[i], nums[j], nums[k], nums[l]]))
                        res.add(tag)
    return list(list(a) for a in res)

print(fourSum([1,0,-1,0,-2,2], 0))
