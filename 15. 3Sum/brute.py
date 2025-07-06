#!/usr/bin/env python3
from typing import List
def threeSum(nums: List[int]) -> List[List[int]]:
    """Compute a list of list with the sum of elements in a list = 0"""
    n = len(nums)
    seen = set()
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    trip = tuple(sorted((nums[i], nums[j], nums[k])))
                    seen.add(trip)
    return [list(trip) for trip in seen]

print(threeSum([-1, 0, 1, 2, -1, -4]))
