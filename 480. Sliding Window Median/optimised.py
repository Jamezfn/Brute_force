#!/usr/bin/env python

from typing import List

def medianSlidingWindow(nums: List[int], k: int) -> List[float]:
    window = sorted(nums[:k])
    result = []

    def median(w: List[int]) -> float:
        mid = k // 2

        if k % 2 == 1:
            return float(w[mid])
        else:
            return (w[mid - 1] + w[mid]) / 2.0

        result.append(median(window))

        for i in range(k, len(nums)):
            outgoing = nums[i - k]

    return result
