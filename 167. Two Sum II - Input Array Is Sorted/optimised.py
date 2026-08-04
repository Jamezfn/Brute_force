#!/usr/bin/env python

from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers) - 1

    while l < r:
        sm = numbers[l] + numbers[r]
        if sm > target:
            r -= 1
        elif sm < target:
            l += 1
        else:
            return [l + 1, r + 1]
    
    return []

print(twoSum([2,7,11,15], 9))
