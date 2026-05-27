#!/usr/bin/env python

from typing import List

def numberOfArithmeticSlices(nums: List[int]) -> int:
    if len(nums) < 3:
        return 0
    count = 0
    n = len(nums)

    for i in range(n):
        for j in range(i + 2, n):
            dif = nums[i + 1] - nums[i]
            ari = True
            for k in range(i + 1, j):
                if nums[k + 1] - nums[k] != dif:
                    ari = False
                    break
            if ari:
                count += 1

    return count


print(numberOfArithmeticSlices([1,2,3,4]))
print(numberOfArithmeticSlices([1,3,5,7,9]))
print(numberOfArithmeticSlices([1]))
