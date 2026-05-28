function characterReplacement(s: string, k: number): number {
	const n = s.length;
	let ans = 0;

	for (let i = 0; i < n; i++) {
		const freq = new Array(26).fill(0);
		let maxFreq = 0;

		for (let j = i; j < n; j++) {
			const idx = s.charCodeAt(j) - 'A'.charCodeAt(0);
			freq[idx]++;

			maxFreq = Math.max(maxFreq, freq[idx]);

			const len = j - i + 1;
			const need = len - maxFreq;

			if (need <= k) {
				ans = Math.max(ans, len);
			}
		}
	}

	return ans;
};


console.log(characterReplacement("ABAB", 2));
console.log(characterReplacement("AABABBA", 1));
