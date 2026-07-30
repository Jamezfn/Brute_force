function minimumRecolors(blocks: string, k: number): number {
	let ans = Infinity;

	for (let i = 0; i < blocks.length - k; i++) {
		let white = 0;
		for (let j = i; j < i + k; j++) {
			if (blocks[j] === "W") {
				white++;
			}
		}

		ans = Math.min(ans, white);
	}

	return ans;
};


console.log(minimumRecolors("WBBWWBBWBW", 7))
