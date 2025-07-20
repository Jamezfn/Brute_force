#!/usr/bin/env python

def isValid(s: str) -> bool:
    """Valid parenthesis using brute force"""
    prev = None
    while prev != s:
        prev = s
        s = s.replace('()', '').replace('{}', '').replace('[]', '')
    return s == ""

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([])"))
print(isValid("([)]"))
