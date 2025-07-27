#!/usr/bin/env python3

from typing import List

def removeDuplicates(nums: List[int]) -> int:
    """
    Brute‑force in‑place removal of duplicates from a sorted list.
    Returns the new length k, with nums[0:k] holding the unique values.
    """
    if not nums:
        return 0

    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1

if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    nd = removeDuplicates(nums)
    print(nd)
    print(nums)
    print(nums[:nd])
