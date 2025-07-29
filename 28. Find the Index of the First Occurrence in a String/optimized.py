#!/usr/bin/env python3

def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)

if __name__ == '__main__':
    print(strStr("sadbutsad", "sad"))
    print(strStr("leetcode", "leeto"))
    print(strStr("jamezs", "mez"))
