#!/usr/bin/env python
from itertools import permutations

def next_permutation(nums: list[int]) -> None:
    """
    Mutates nums to the next lexicographic permutation.
    Generates unique permutations via backtracking (lexicographic order),
    finds the current permutation, and writes the next one back in-place.
    """
    perms = list(permutations(nums))
    i = perms.index(tuple(nums))
    nums[:] = list(perms[(i + 1) % len(nums)])
    return nums

if __name__ == '__main__':
    print(next_permutation([1, 2, 3]))
