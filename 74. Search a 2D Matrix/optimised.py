#!/usr/bin/env python

from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])

    l, r = 0, rows * cols - 1

    while l <= r:
        mid = (l + r) // 2

        row = mid // cols
        col = mid % cols

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            l = mid + 1
        else:
            r = mid - 1

    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20]], 3))
