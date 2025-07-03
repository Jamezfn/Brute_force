#!/usr/bin/env python3

def intToRoman(num:int) -> str:
    """Computes the roman number using brute force"""
    vals = [
        (1000, "M"), (900, "CM"),
        (500,  "D"), (400, "CD"),
        (100,  "C"), (90,  "XC"),
        (50,   "L"), (40,  "XL"),
        (10,   "X"), (9,   "IX"),
        (5,    "V"), (4,   "IV"),
        (1,    "I"),
    ]

    roman = []
    for value, symbol in vals:
        while num >= value:
            roman.append(symbol)
            num -= value
        if num == 0:
            break
    return "".join(roman)

print(intToRoman(3749))
