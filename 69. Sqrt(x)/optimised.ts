function mySqrt(x: number): number {
	let [i, j] = [0, x];

	while (i <= j) {
		const mid = Math.floor((i + j) / 2);
		const square = mid * mid;

		if (square == x) {
			return mid;
		} else if (square < x) {
			i = mid + 1;
		} else {
			j = mid - 1;
		}
	}

	return j;
};

console.log(mySqrt(8));
