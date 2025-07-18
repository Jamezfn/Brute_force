#!/usr/bin/env python3
from typing import List
def threeSum(nums: List[int]) -> List[List[int]]:
    """Compute a list of list with the sum of 3 ints in the list = 0"""
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        target = -nums[i]
        L, R = i + 1, n - 1
        while L < R:
            s = nums[L] + nums[R]
            if s < target:
                L += 1
            elif s > target:
                R -= 1
            else:
                res.append([nums[i], nums[L], nums[R]])
                while L < R and nums[L] == nums[L+1]:
                    L += 1
                while L < R and nums[R] == nums[R-1]:
                    R -= 1
                L += 1
                R -= 1
    return res
print(threeSum([-1, 0, 1, 2, -1, -4]))
