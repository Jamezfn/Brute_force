#!/usr/bin/env python

from typing import List

def search(nums: List[int], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            return i


print(search([4,5,6,7,0,1,2], 0))
