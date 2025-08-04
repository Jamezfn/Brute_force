#!/usr/bin/env python

from typing import List
from collections import Counter

def findSubstring(s: str, words: List[str]) -> List[int]:
    """Substring with Concatenation of All Words using brute force"""
    word_len = len(words[0])
    num_words = len(words)
    window_len = word_len * num_words
    target = Counter(words)
    result = []
    for offset in range(word_len):
        left = offset
        curr = Counter()
        count = 0

        for right in range(offset, len(s) - word_len + 1, word_len):
            w = s[right:right + word_len]
            if w in target:
                curr[w] += 1
                count += 1

                while curr[w] > target[w]:
                    left_w = s[left:left + word_len]
                    curr[left_w] -= 1
                    left += word_len
                    count -= 1

                if count == num_words:
                    result.append(left)
                    left_w = s[left:left + word_len]
                    curr[left_w] -= 1
                    left += word_len
                    count -= 1
            else:
                curr.clear()
                count = 0
                left = right + word_len
    return result

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
