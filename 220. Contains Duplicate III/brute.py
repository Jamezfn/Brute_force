#!/usr/bin/env python

from typing import List

def containsNearbyAlmostDuplicate(nums: List[int], indexDiff: int, valueDiff: int) -> bool:
    """Contains Duplicate III"""
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, min(indexDiff + 1, n)):
            if abs(nums[i] - nums[j]) <= valueDiff:
                return True

    return False

print(containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))
print(containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))
