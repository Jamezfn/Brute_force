function decrypt(code: number[], k: number): number[] {
	const n = code.length;
	const res: number[] = new Array(n).fill(0);
	for (let i = 0; i < n; i++) {
		if (k > 0) {
			for (let j = i + 1; j <= i + Math.abs(k); j++) {
				res[i] += code[j % n];
			}
		} else if (k < 0) {
			for (let j = i - 1; j >= i - Math.abs(k); j--) {
				res[i] += code[((j % n) + n) % n];
			}
		}
	}

	return res;
};

console.log(decrypt([5,7,1,4], 3))
console.log(decrypt([1,2,3,4], 0))
console.log(decrypt([2,4,9,3], -2))

