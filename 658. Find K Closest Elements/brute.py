#!/usr/bin/env python

from typing import List

def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    nums = []
    for num in arr:
        nums.append((abs(num - x), num))

    nums.sort()

    res = []
    for i in range(k):
        res.append(nums[i][1])
    res. sort()

    return res

print(findClosestElements([1,2,3,4,5], 4, 3))
