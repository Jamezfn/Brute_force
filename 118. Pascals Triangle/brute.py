#!/usr/bin/env python

from typing import List

def generate(numRows: int) -> List[List[int]]:
    triangle = []
    for row in range(numRows):
        current = []

        for col in range(row + 1):
            if col == 0 or row == col:
                current.append(1)
            else:
                current.append(triangle[row - 1][col] + triangle[row - 1][col - 1])

        triangle.append(current)

    return triangle

print(generate(5))
