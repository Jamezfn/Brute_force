#!/usr/bin/env python

from typing import List
from collections import Counter

def findSubstring(s: str, words: List[str]) -> List[int]:
    """Substring with Concatenation of All Words using brute force"""
    word_len = len(words[0])
    num_words = len(words)
    window_len = word_len * num_words
    results = []
    for i in range(0, len(s) - window_len + 1):
        substring = s[i:i + window_len]
        chunks = [substring[j:j+word_len] for j in range(0, window_len, word_len)]
        if Counter(chunks) == Counter(words):
            results.append(i)
    return results

if __name__ == '__main__':
    s = "barfoothefoobarman"
    words = ["foo","bar"]
    print(findSubstring(s, words))

    s2 = "wordgoodgoodgoodbestword"
    words2 = ["word","good","best","word"]
    print(findSubstring(s2, words2))

    s3 = "barfoofoobarthefoobarman"
    words3 = ["bar","foo","the"]
    print(findSubstring(s3, words3))

    s4 = "barfoothefoobarman"
    words4 = ["foo", "bar"]
    print(findSubstring(s4, words4))
