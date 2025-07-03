#!/usr/bin/env python3
from typing import List
def maxArea(height:List[int]) -> int:
    """Compute max area using Two pointers Algorithmn"""
    left = 0
    right = len(height) - 1
    res = 0
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        area = width * h
        res = max(res, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return res

a = maxArea([1,8,6,2,5,4,8,3,7])
print(a)
