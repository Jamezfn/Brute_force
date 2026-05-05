#!/usr/bin/env python

from typing import List

def minSubArrayLen(target: int, nums: List[int]) -> int:
    """209. Minimum Size Subarray Sum"""
    n = len(nums)
    ans = float('inf')

    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]

            if total >= target:
                ans = min(ans, j - i + 1)
                break

    return 0 if ans == float("inf") else ans

print(minSubArrayLen(4, [1,4,4]))

print(minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
