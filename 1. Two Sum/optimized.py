#!/usr/bin/env python

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    """Compute indices of two number whose sum is target"""
    seen = {}
    for i, num in enumerate(nums):
        dif = target - num
        if dif in seen:
            return [seen[dif], i]
        seen[num] = i

if __name__ == '__main__':
    print(twoSum([2, 7, 11, 15], 9));
    print(twoSum([3, 2, 4], 6));
    print(twoSum([3, 3], 6));
