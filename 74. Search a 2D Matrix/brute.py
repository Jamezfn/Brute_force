#!/usr/bin/env python

from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    for row in matrix:
        for num in row:
            if num == target:
                return True

    return false

print(searchMatrix([[1,3,5,7],[10,11,16,20]], 3))
