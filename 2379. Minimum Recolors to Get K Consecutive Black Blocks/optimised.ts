function minimumRecolors(blocks: string, k: number): number {
	let white = 0;

	for (let i = 0; i < k; i++) {
		if (blocks[i] === "W") white++;
	}

	let ans = white;

	for (let i = k; i < blocks.length; i++) {
		if (blocks[i - k] === "W") {
			white--;
		}

		if (blocks[i] === "W") {
                        white++;
                }

		ans = Math.min(ans, white);
	}

	return ans;
};

console.log(minimumRecolors("WBBWWBBWBW", 7))
