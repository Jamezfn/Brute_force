/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var longestSubstring = function(s, k) {
    if (s.length < k) {
        return 0;
    }

    const freq = new Map();
    for (const c of s) {
        freq.set(c, (freq.get(c) || 0) + 1);
    }

    if ([...freq.values()].every(v => v >= k)) {
        return s.length;
    }

    let result = 0;
    let start = 0;

    for (let i = 0; i < s.length; i++) {
        if (freq.get(s[i]) < k) {
            result = Math.max(result, longestSubstring(s.slice(start, i), k));
            start = i + 1;
        }
    }

    result = Math.max(result, longestSubstring(s.slice(start), k));

    return result;
};

console.log(longestSubstring("aaabb", 3));   // 3
console.log(longestSubstring("ababbc", 2));   // 5
