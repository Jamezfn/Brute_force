#!/usr/bin/env python3
from typing import List
def maxArea(height: List[int]) -> int:
    """Compute maximum area from a list with brute force"""
    res = 0
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            area = (j - i) * min(height[i], height[j])
            res = max(res, area)
    return res

a = maxArea([1,8,6,2,5,4,8,3,7])
print(a)
