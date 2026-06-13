#!/usr/bin/env python

from typing import List

def sortColors(nums: List[int]) -> None:
    n = len(nums)

    for i in range(n):
        for j in range(n - 1 - i):
            if nums[j + 1] < nums[j]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)
