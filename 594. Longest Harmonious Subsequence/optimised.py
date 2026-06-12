#!/usr/bin/env python

from typing import List

def findLHS(nums: List[int]) -> int:
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    ans = 0
    for num in freq:
        if num + 1 in freq:
            ans = max(ans, freq[num] + freq[num + 1])

    return ans

print(findLHS([1,3,2,2,5,2,3,7]))
