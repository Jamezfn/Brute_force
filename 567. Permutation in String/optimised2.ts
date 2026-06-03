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

	let matches = 0;
	for (let i = 0; i < 26; i++) {
		if (s1Count[i] === s2Count[i]) matches++;
	}

	let l = 0;

	for (let r = n; r < m; r++) {
		if (matches === 26) return true;

		let idx = s2.charCodeAt(r) - a;
		s2Count[idx]++;

		if (s2Count[idx] === s1Count[idx]) {
			matches++;
		}
		else if (s1Count[idx] + 1 === s2Count[idx]) {
			matches--;
		}

		idx = s2.charCodeAt(l) - a;
		s2Count[idx]--;

                if (s2Count[idx] === s1Count[idx]) {
                        matches++;
                }
                else if (s1Count[idx] - 1 === s2Count[idx]) {
                        matches--;
                }

		l++

	}

	return matches === 26; 
}

console.log(checkInclusion("ab", "eidbaooo"));
console.log(checkInclusion("ab", "eidboaoo"));
