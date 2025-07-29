#!/usr/bin/env node

/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
	if (haystack.length === 0) {
		return 0;
	}

	if (haystack.length < needle.length) {
		return -1
	}

	for (let i = 0; i < haystack.length - needle.length + 1; i++) {
		let match = true;
		for (let = j = 0; j < needle.length; j++) {
			if (haystack[i + j] !== needle[j]) {
				match = false;
				break;
			}
		}
		if (match) {
			return i;
		}
	}
	return -1;
};

console.log(strStr("sadbutsad", "sad"));
console.log(strStr("leetcode", "leeto"));
console.log(strStr("jamezs", "mez"));
