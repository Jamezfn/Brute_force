#!/usr/bin/env python3

def strStr(haystack: str, needle: str) -> int:
    h, n = len(haystack), len(needle)
    if h == 0:
        return 0

    for i in range(h - n + 1):
        match = True
        for j in range(n):
            if haystack[i + j] != needle[j]:
                match = False
                break
        if match:
            return i

    return -1

if __name__ == '__main__':
    print(strStr("sadbutsad", "sad"))
    print(strStr("leetcode", "leeto"))
    print(strStr("jamezs", "mez"))
