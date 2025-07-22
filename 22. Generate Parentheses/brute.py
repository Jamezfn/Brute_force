#!/usr/bin/env python

from typing import List

def generateParenthesis(n: int) -> List[str]:
    """Generate parenthesis using brute force"""
    def is_valid(seq):
        """Check if the sequence is well formed"""
        bal = 0
        for ch in seq:
            if ch == '(':
                bal += 1
            else:
                bal -= 1
            if bal < 0:
                return False

        return bal == 0
    
    results = []
    def backtrack(curr):
        """Build every possible sequence"""
        if len(curr) == n * 2:
            if is_valid(curr):
                results.append(curr)
            return
        backtrack(curr + '(')
        backtrack(curr + ')')

    backtrack("")
    return results

if __name__ == '__main__':
    print(generateParenthesis(3))
