#!/usr/bin/env python

from typing import List

def medianSlidingWindow(nums: List[int], k: int) -> List[float]:
    n = len(nums)
    result = []
    for i in range(n - k + 1):
        window = nums[i:i + k]
        window.sort()

        if k % 2 == 1:
            median = float(window[k // 2])
        else:
            median = (window[k // 2 - 1] + window[k // 2]) / 2

        result.append(median)

    return result

print(medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
