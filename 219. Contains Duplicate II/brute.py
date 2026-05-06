#!/usr/bin/env python

from typing import List

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    """Contains Duplicate II"""
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j] and abs(i - j) <= k:
                return True
    return False

print(containsNearbyDuplicate([1,2,3,1], k=3))
print(containsNearbyDuplicate([1,0,1,1], k=1))
print(containsNearbyDuplicate([1,2,3,1,2,3], k=2))
