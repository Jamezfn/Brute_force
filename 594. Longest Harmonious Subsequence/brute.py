#!/usr/bin/env python

from typing import List

def findLHS(nums: List[int]) -> int:
    n = len(nums)
    ans = 0

    def dfs(i, seq):
        nonlocal ans

        if seq and max(seq) - min(seq) == 1:
            ans = max(ans, len(seq))

        if i == n:
            return

        seq.append(nums[i])
        dfs(i + 1, seq)

        seq.pop()
        dfs(i + 1, seq)


    dfs(0, [])

    return ans

print(findLHS([1,3,2,2,5,2,3,7]))
