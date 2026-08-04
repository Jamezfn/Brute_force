#!/usr/bin/env python

from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    n = len(numbers)
    
    for i in range(n):
        for j in range(i + 1, n):
            sm = numbers[i] + numbers[j]
            if sm == target:
                return [i + 1, j + 1]

print(twoSum([2,7,11,15], 9))
