function findAnagrams(s: string, p: string): number[] {
	const lenP = p.length;
	const countP: Record<string, number> = {};
	for (const ch of p) countP[ch] = (countP[ch] ?? 0) + 1;

	const res: number[] = [];

	for (let i = 0; i <= s.length - lenP; i++) {
		const window = s.slice(i, i + lenP);
		const countW: Record<string, number> = {};
		for (const ch of window) countW[ch] = (countW[ch] ?? 0) + 1;

		const isAnagram =
            		Object.keys(countP).length === Object.keys(countW).length &&
            		Object.entries(countP).every(([k, v]) => countW[k] === v);

		if (isAnagram) res.push(i);
	}

	return res;
}

console.log(findAnagrams("cbaebabacd", "abc"));
