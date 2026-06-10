#!/usr/bin/env python

from typing import List

def jump(nums: List[int]) -> int:
    n = len(nums)

    def dfs(i):
        if i >= n - 1:
            return 0
        min_jumps = float('inf')

        for jump in range(1, nums[i] + 1):
            min_jumps = min(min_jumps, 1 + dfs(i + jump))

        return min_jumps

    return dfs(0)


print(jump([2,3,1,1,4]))
