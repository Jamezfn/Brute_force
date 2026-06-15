#!/usr/bin/env python

from typing import List

def removeDuplicates(nums: List[int]) -> int:
    n = len(nums)
    if n <= 2:
        return n

    k = 2
    for i in range(2, n):
        if nums[i] != nums[k - 2]:
            nums[k] = nums[i]
            k += 1

    return k

print(removeDuplicates([1,1,1,2,2,3]))
