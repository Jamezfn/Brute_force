#!/usr/bin/env python

from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()

    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l = i + 1
        r = len(nums) - 1

        while l < r:
            tt = nums[i] + nums[l] + nums[r]
            if tt < 0:
                l += 1
            elif tt > 0:
                r -+ 1
            else:
                result.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
            l += 1
            r -= 1

    return result

print(threeSum([-1,0,1,2,-1,-1]))
