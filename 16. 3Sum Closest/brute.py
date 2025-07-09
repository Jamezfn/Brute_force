#!/usr/bin/env python3
from typing import List

def threeSumClosest(nums: List[int], target: int) -> int:
    """Compute the closest sum from a list close to target + Brute force"""
    n = len(nums)
    res = nums[0] + nums[1] + nums[2]
    min_dif = abs(res - target)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                s = nums[i] + nums[j] + nums[k]
                dif = abs(s - target)
                if dif < min_dif:
                    min_dif = dif
                    res = s
                if dif == 0:
                    return s
    return res
if __name__ == '__main__':
    print(threeSumClosest([-1,2,1,-4], 1))
