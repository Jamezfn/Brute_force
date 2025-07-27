#!/usr/bin/env python3

from typing import List

def removeDuplicates(nums: List[int]) -> int:
    """
    Brute‑force in‑place removal of duplicates from a sorted list.
    Returns the new length k, with nums[0:k] holding the unique values.
    """
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            nums.pop(i + 1)
        else:
            i += 1

    return len(nums)

nums = [0,0,1,1,1,2,2,3,3,4]
nd = removeDuplicates(nums)
print(nd)
print(nums)
