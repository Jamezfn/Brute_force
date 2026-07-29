function divisorSubstrings(num: number, k: number): number {
	const s = num.toString();
    	let count = 0;

	for (let i = 0; i <= s.length - k; i++) {
		let sub = Number(s.slice(i, i + k));

		if (sub !== 0 && num % sub === 0) {
			count++;
		}
	}

	return count;
};

console.log(divisorSubstrings(240, 2));
