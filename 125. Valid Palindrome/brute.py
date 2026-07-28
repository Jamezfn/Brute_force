#!/usr/bin/env python

def isPalindrome(s: str) -> bool:
    clean = ""
    for char in s:
        if char.isalnum():
            clean += char.lower()

    return clean == clean[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"))
