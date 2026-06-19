#!/usr/bin/env python

from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:
    res = []
    for i in range(len(nums)):
        if nums[i] == target:
            res.append(i)

    return res

print(searchRange([5,7,7,8,8,10], 8))
