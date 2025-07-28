#!/usr/bin/env python

from typing import List

def removeElement(nums: List[int], val: int) -> int:
    """
    Remove all occurrences of val in‑place by shifting.
    Returns the new “length” k; nums[0:k] are the kept values.
    """
    n = len(nums)
    i = 0
    while i < n:
        if nums[i] == val:
            for j in range(i, n-1):
                nums[j] = nums[j + 1]
            n -= 1
        else:
            i += 1
    return n

if __name__ == '__main__':
    arr1 = [3,2,2,3]
    k1 = removeElement(arr1, 3)
    print(k1, arr1[:k1])

    arr2 = [0,1,2,2,3,0,4,2]
    k2 = removeElement(arr2, 2)
    print(k2, arr2[:k2])
