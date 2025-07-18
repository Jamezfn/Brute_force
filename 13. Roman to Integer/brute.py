#!/usr/bin/env python3
def romanToInt(s: str) -> int:
    """Computes roman to int using brute force"""
    vals = [
        (1000, "M"), (900, "CM"),
        (500,  "D"), (400, "CD"),
        (100,  "C"), (90,  "XC"),
        (50,   "L"), (40,  "XL"),
        (10,   "X"), (9,   "IX"),
        (5,    "V"), (4,   "IV"),
        (1,    "I"),
    ]
    res = 0
    while s:
        for value, sym in vals:
            if s.startswith(sym):
                res += value
                s = s[len(sym):]
                #break
    return res

print(romanToInt('MMMMMMCMXCIV'))
