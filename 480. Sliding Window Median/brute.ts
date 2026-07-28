function medianSlidingWindow(nums: number[], k: number): number[] {
	const n = nums.length;
	const result = [];
	for (let i = 0; i < n - k + 1; i++) {
		const window = nums.slice(i, i + k);
		window.sort((a, b) => a - b);

		let median: number;

		if (k % 2 === 1) {
			median = window[Math.floor(k / 2)];
		} else {
			median = (window[k / 2 - 1] + window[k / 2]) / 2;
		}

		result.push(median);
	}

	return result;
};

console.log(medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3));
