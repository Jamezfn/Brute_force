#!/usr/bin/env python

from typing import List

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    """Contains Duplicate II"""
    window = set()

    for i, num in enumerate(nums):
        if num in window:
            return True

        window.add(num)
        if len(window) > k:
            window.remove(nums[i - k])

    return False

print(containsNearbyDuplicate([1,2,3,1], k=3))
print(containsNearbyDuplicate([1,0,1,1], k=1))
print(containsNearbyDuplicate([1,2,3,1,2,3], k=2))
