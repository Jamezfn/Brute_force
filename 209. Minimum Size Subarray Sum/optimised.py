#!/usr/bin/env python

from typing import List

def minSubArrayLen(target: int, nums: List[int]) -> int:
    n = len(nums)
    left = 0
    total = 0
    ans = float('inf')

    for right in range(n):
        total += nums[right]

        while total >= target:
            ans = min(ans, right - left + 1)
            total -= nums[left]
            left += 1

    return 0 if ans == float('inf') else ans

print(minSubArrayLen(4, [1,4,4]))

print(minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
