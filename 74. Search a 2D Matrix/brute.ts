function searchMatrix(matrix: number[][], target: number): boolean {
	for (const row of matrix) {
		for (const num of row) {
			if (num === target) {
				return true;
			}
		}
	}

	return true;
};

console.log(searchMatrix([[1,3,5,7],[10,11,16,20]], 3))
