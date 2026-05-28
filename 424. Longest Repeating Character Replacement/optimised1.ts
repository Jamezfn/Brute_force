function characterReplacement(s: string, k: number): number {
	const count = new Array(26).fill(0);

	let res: number = 0;
	let maxf = 0;
	let l = 0;
	for (let r = 0; r < s.length; r++) {
		const idx = s.charCodeAt(r) - 'A'.charCodeAt(0);

		count[idx]++;
		maxf = Math.max(maxf, count[idx]);

		while ((r - l + 1) - maxf > k) {
			count[s.charCodeAt(l) - 65]--;
			l++;
		}

		res = Math.max(res, r - l + 1);

	}

	return res;
}

console.log(characterReplacement("ABAB", 2));
console.log(characterReplacement("AABABBA", 1));
