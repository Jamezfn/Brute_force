function searchMatrix(matrix: number[][], target: number): boolean {
	const [rows, cols] = [matrix.length, matrix[0].length];

	let [l, r] = [0, rows * cols - 1];

	while (l <= r) {
		const mid = Math.floor((l + r) / 2);

		const row = Math.floor(mid / cols);
		const col = mid % cols;

		if (matrix[row][col] === target) {
			return true;
		}
		else if (matrix[row][col] < target) {
			l = mid + 1;
		}
		else {
			r = mid - 1;
		}
	}

	return false;
};

console.log(searchMatrix([[1,3,5,7],[10,11,16,20]], 3));
