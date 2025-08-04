#!/usr/bin/env node
/**
 * @param {string} s
 * @param {string[]} words
 * @return {number[]}
 */

function countWords(arr) {
	const count = {};
	for (const word of arr) {
		count[word] = (count[word] || 0) + 1;
	}
	return count;
}

function isEqualMap(a, b) {
    if (Object.keys(a).length !== Object.keys(b).length) return false;
    for (const key in a) {
        if (a[key] !== b[key]) return false;
    }
    return true;
}

var findSubstring = function(s, words) {
	const word_len = words[0].length;
	const num_words = words.length;
	const window_len = word_len * num_words;

	const results = [];
	for (let i = 0; i <= s.length - window_len; i++) {
		const substring = s.slice(i, i + window_len);
		const chunks = [];
		for (let j = 0; j < window_len; j += word_len) {
			chunks.push(substring.slice(j, j + word_len));
		}
		if (isEqualMap(countWords(chunks), countWords(words))) {
			results.push(i);
		}
	}

	return results;
};

console.log(findSubstring("barfoothefoobarman", ["foo", "bar"]))
