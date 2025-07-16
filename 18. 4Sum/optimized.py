#!/usr/bin/env python

from typing import List

def fourSum(nums: List[int], target: int) -> List[List[int]]:
    """Compute a list of 4 integer list: sum of integers add up target"""
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, n-2):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            L, R = j+1, n-1
            while L < R:
                s = nums[i] + nums[j] + nums[L] + nums[R]
                if s < target:
                    L += 1
                elif s == target:
                    res.append([nums[i], nums[j], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L - 1]:
                        left += 1
                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1
                else:
                    R -= 1
    return res

print(fourSum([2,2,2,2,2], 8))
print(fourSum([1,0,-1,0,-2,2], 0))
