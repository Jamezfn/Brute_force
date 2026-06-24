#!/usr/bin/env python

from typing import List

def numSubarraysWithSum(nums: List[int], goal: int) -> int:
    n = len(nums)
    ans = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += nums[j]
            if sum > goal:
                break

            if sum == goal:
                ans += 1

    return ans

print(numSubarraysWithSum([1,0,1,0,1], 2))
