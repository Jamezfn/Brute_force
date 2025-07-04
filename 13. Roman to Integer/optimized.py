#!/usr/bin/env python3
def romanToInt(s: str) -> int:
    """computes roman to integer using a Stack algorithm"""
    vals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    stack = []
    for ch in s:
        current = vals[ch]
        if stack and stack[-1] < current:
            prev = stack.pop()
            stack.append(current - prev)
        else:
            stack.append(current)
    return sum(stack)
print(romanToInt('MCMXCIV'))
