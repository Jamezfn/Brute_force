function exist(board: string[][], word: string): boolean {
	const ROWS = board.length;
	const COLS = board[0].length;
	const path = new Set<number>();

	function dfs(r: number, c: number, i: number): boolean {
		if (i === word.length) {
			return true;
		}

		if (r < 0 || c < 0 || r >= ROWS || c >= COLS || path.has(r * COLS + c) || board[r][c] !== word[i]) {
			return false;
		}

		path.add(r * COLS + c);

		const res = (
			dfs(r + 1, c, i + 1) || dfs(r - 1, c, i + 1) ||
			dfs(r, c + 1, i + 1) || dfs(r, c - 1, i + 1)
		);

		path.delete(r * COLS + c);

		return res;
	}

	for (let r = 0; r < ROWS; r++) {
		for (let c = 0; c < COLS; c++) {
			if (dfs(r, c, 0)) {
				return true;
			}
		}
	}

	return false;
};

console.log(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))