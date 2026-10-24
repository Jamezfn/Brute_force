#!/usr/bin/env python

from typing import List

def triangleNumber(nums: List[int]) -> int:
    nums.sort()

    count = 0

    for i in range(len(nums) - 1, 1, -1):
        l = 0
        r = i - 1

        while l < r:
            if nums[l] + nums[r] > nums[i]:
                count += r - l
                r -= 1
            else:
                l += 1

    return count


print(triangleNumber([11,4,9,6,15,18]))
