/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var longestSubstring = function(s, k) {
	const n = s.length
	let ans = 0;

	for (let i = 0; i <= n; i++) {
		for (let j = i + 1; j <= n; j++) {
			const substring = s.slice(i, j);
			const freq = {};

			for (const c of substring) {
				freq[c] = (freq[c] || 0) + 1;
			}

			if (Object.values(freq).every(count => count >= k)) {
				ans = Math.max(ans, substring.length);
			}
		}
	}

	return ans
};

console.log(longestSubstring("aaabb", 3));
console.log(longestSubstring("ababbc", 2));
