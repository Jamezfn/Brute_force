#!/usr/bin/env python

from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] >= target:
            return i


print(searchInsert([1,3,5,6], 5))
