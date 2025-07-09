#!/usr/bin/env python3
from typing import List
def threeSumClosest(nums: List[int], target: int) -> int:
    """Compute the closest some to the target with sort+pointer algorithmn"""
    nums.sort()
    n = len(nums)
    closest = nums[0] + nums[1] + nums[2]
    for i in range(n-2):
        l, r = i+1, n-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if abs(s - target) < abs(closest - target):
                closest = s
            if s < target:
                l += 1
            else:
                return s

    return closest

if __name__ == '__main__':
    print(threeSumClosest([-1, 2, 1, -4], 1))
