#!/usr/bin/env python

from typing import List

def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    n = len(nums)
    count = 0
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= nums[j]
            if product < k:
                count += 1

    return count

print(numSubarrayProductLessThanK([10,5,2,6], 100))
print(numSubarrayProductLessThanK([1,2,3], 0))
