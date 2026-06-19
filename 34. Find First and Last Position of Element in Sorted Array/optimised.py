#!/usr/bin/env python

from typing import List

def binary(nums: List, target: int, first: bool) -> int:
    l, r = 0, len(nums) - 1
    i = -1
    while l <= r:
        mid = (l + r) // 2

        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            i = mid
            if first:
                r = mid - 1
            else:
                l = mid + 1

    return i

def searchRange(nums: List[int], target: int) -> List[int]:
    return [binary(nums, target, True), binary(nums, target, False)]

print(searchRange([5,7,7,8,8,10], 8))

