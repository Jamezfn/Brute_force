#!/usr/bin/env python

import bisect
from typing import List

def minSubArrayLen(target: int, nums: List[int]) -> int:
    """Minimum Size Subarray Sum"""
    n = len(nums)
    prefix = [0] * (n + 1)
    ans = float('inf')

    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    for i in range(n):
        needed = prefix[i] + target
        j = bisect.bisect_left(prefix, needed)

        if j <= n:
            ans = min(ans, j - i)

    return 0 if ans == float("inf") else ans


print(minSubArrayLen(4, [1,4,4]))

print(minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
