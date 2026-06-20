#!/usr/bin/env python

from typing import List

def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    if k < 1:
        return 0

    product = 1
    count = 0
    i = 0
    for j in range(len(nums)):
        product *= nums[j]

        while i <= j and product >= k:
            product //= nums[i]
            i += 1

        count += j - i + 1

    return count

print(numSubarrayProductLessThanK([10,5,2,6], 100))
print(numSubarrayProductLessThanK([1,2,3], 0))
