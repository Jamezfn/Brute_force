#!/usr/bin/env python

from typing import List

def removeElement(nums: List[int], val: int) -> int:
    """
    Remove all occurrences of val in‑place by shifting.
    Returns the new “length” k; nums[0:k] are the kept values.
    """
    slow = 0
    for fast in range(slow, len(nums) - 1):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    return slow
if __name__ == '__main__':
    arr1 = [3,2,2,3]
    k1 = removeElement(arr1, 3)
    print(k1, arr1[:k1])

    arr2 = [0,1,2,2,3,0,4,2]
    k2 = removeElement(arr2, 2)
    print(k2, arr2[:k2])
