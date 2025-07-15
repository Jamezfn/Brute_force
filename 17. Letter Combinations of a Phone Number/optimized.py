#!/usr/bin/env python

def letterCombinations(digits: str) -> list[str]:
    """List all letter combinations of a phone Number using recursion"""
    if not digits or digits == str(1):
        return []

    map_d = {
        '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
        '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
    }
    res = []
    path = []

    def backtrack(index: int):
        if index == len(digits):
            res.append(''.join(path))
            return
        
        pos_let = map_d[digits[index]]
        for ch in pos_let:
            path.append(ch)
            backtrack(index+1)
            path.pop()


    backtrack(0)
    return res


print(letterCombinations("1"))
print(letterCombinations(""))
print(letterCombinations("2"))
print(letterCombinations("24"))
print(letterCombinations("79"))
