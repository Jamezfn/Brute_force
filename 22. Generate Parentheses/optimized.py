#!/usr/bin/env python3

from typing import List

def generateParenthesis(n: int) -> List[str]:
    """Generate parenthesis using pruned backtracking"""
    results = []
    def backtrack(curr, open_count, close_count):
        if len(curr) == 2 * n:
            results.append(curr)
            return

        if open_count < n:
            backtrack(curr + '(', open_count + 1, close_count)

        if close_count < open_count:
            backtrack(curr + ')', open_count, close_count + 1)

    backtrack("", 0, 0)
    return results

if __name__ == '__main__':
    print(generateParenthesis(3))
