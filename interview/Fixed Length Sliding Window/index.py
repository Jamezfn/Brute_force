#!/usr/bin/env python

from typing import List

def max_subarray_sum(nums: List[int], k: int):
    max_sum = float("-inf")
    state = 0
    start = 0

    for end in range(len(nums)):
        state += nums[end]
        if end - start + 1 == k:
            max_sum = max(max_sum, state)
            state -= nums[start]
            start += 1

    return max_sum

print(max_subarray_sum([2, 1, 5, 1, 3, 2], 3))
