#!/usr/bin/env python
from typing import List
def letterCombinations(digits: str) -> List[str]:
    """
    Return all possible letter combination of
    a phone number using brute force
    """
    if digits is None or digits == str(1):
        return []
    map_d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
            }

    letters = [map_d[d] for d in digits]
    res = []
    if len(letters) == 1:
        for c1 in letters[0]:
            res.append(c1)
    elif len(letters) == 2:
        for c1 in letters[0]:
            for c2 in letters[1]:
                res.append(c1 + c2)
    elif len(letters) == 3:
        for c1 in letters[0]:
            for c2 in letters[1]:
                for c3 in letters[2]:
                    res.append(c1 + c2 + c3)
    elif len(letters) == 3:
        for c1 in letters[0]:
            for c2 in letters[1]:
                for c3 in letters[2]:
                    for c4 in letters[3]:
                        res.append(c1 + c2 + c3 + c4)
    return res

print(letterCombinations("1"))
print(letterCombinations(""))
print(letterCombinations("2"))
print(letterCombinations("24"))
print(letterCombinations("79"))
