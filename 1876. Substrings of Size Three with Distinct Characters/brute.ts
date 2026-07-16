function countGoodSubstrings(s: string): number {
	let ans = 0;
	
	for (let i = 0; i < s.length - 2; i++) {
		if (s[i] !== s[i+1] && s[i+1] !== s[i+2] && s[i] !== s[i+2]) {
			ans++;
		}
	}

	return ans;
};

console.log(countGoodSubstrings("xyzzaz"));
console.log(countGoodSubstrings("aababcabc"));
