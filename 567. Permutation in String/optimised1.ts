function checkInclusion(s1: string, s2: string): boolean {
	const n = s1.length;
	const m = s2.length;

	if (n > m) return false;

	const s1Count = new Array(26).fill(0);
	const s2Count = new Array(26).fill(0);
	const a = 'a'.charCodeAt(0);

	for (let i = 0; i < n; i++) {
		s1Count[s1.charCodeAt(i) - a]++;
		s2Count[s2.charCodeAt(i) - a]++;
	}

	if (s1Count.join() === s2Count.join()) return true;

	for (let i = n; i < m; i++) {
		s2Count[s2.charCodeAt(i) - a]++;
		s2Count[s2.charCodeAt(i - n) - a]--;

		if (s1Count.join() === s2Count.join()) return true;
	}

	return false;
};

console.log(checkInclusion("ab", "eidbaooo"));
console.log(checkInclusion("ab", "eidboaoo"));
