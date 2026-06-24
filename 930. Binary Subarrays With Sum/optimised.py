#!/usr/bin/env python

from typing import List

def numSubarraysWithSum(nums: List[int], goal: int) -> int:
    def atMost(x):
        n = len(nums)
        ans = 0
        total = 0
        i = 0
        for j in range(n):
            total += nums[j]
            while total > x:
                total -= nums[i]
                i += 1

            ans += j - i + 1

        return ans

    return atMost(goal) - atMost(goal - 1)

print(numSubarraysWithSum([1,0,1,0,1], 2))
