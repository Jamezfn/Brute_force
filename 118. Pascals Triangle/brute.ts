function generate(numRows: number): number[][] {
	const tri: number[][] = [];

	for (let i = 0; i < numRows; i++) {
		const cur: number[] = [];

		for (let j = 0; j < i + 1; j++) {
			if (j == 0 || j == i) {
				cur.push(1);
			} else {
				cur.push(tri[i - 1][j] + tri[i - 1][j - 1]);
			}
		}

		tri.push(cur);
	}

	return tri;
};

console.log(generate(5));
