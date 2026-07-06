function decrypt(code: number[], k: number): number[] {
	const n = code.length;
	let sm = 0;
	let l = 0;
	const res: number[] = new Array(n).fill(0);
	for (let r = 0; r < n + Math.abs(k); r++) {
		sm += code[r % n];

		if (r - l + 1 > Math.abs(k)) {
			sm -= code[l % n];
			l = (l + 1) % n;
		}

		if (r - l + 1 == Math.abs(k)) {
			if (k > 0) {
				res[((l - 1) + n) % n] = sm;
			}
			else if (k < 0) {
				res[((r + 1) + n) % n] = sm;
			}
		}
	}

	return res;
};

console.log(decrypt([5,7,1,4], 3))
console.log(decrypt([1,2,3,4], 0))
console.log(decrypt([2,4,9,3], -2))

