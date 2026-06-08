#!/usr/bin/env python

from typing import List

def canJump(nums: List[int]) -> bool:
    n = len(nums)

    def dfs(i):
        if i >= n - 1:
            return True

        for jump in range(1, nums[i] + 1):
            if dfs(i + jump):
                return True

        return False

    return dfs(0)

print(canJump([2,3,1,1,4]))
