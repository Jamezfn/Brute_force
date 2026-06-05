#!/usr/bin/env python

from typing import List

def trap(height: List[int]) -> int:
    n = len(height)
    water = 0

    for i in range(n):
        left_max = 0
        right_max = 0

        for l in range(i):
            left_max = max(left_max, height[l])

        for r in range(i + 1, n):
            right_max = max(right_max, height[r])


        water += max(min(left_max, right_max) - height[i], 0)


    return water

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([4,2,0,3,2,5]))
