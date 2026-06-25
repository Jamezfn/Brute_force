function findMaxAverage(nums: number[], k: number): number {
	let window_sum: number = nums.slice(0, k).reduce((a, b) => a + b, 0);
	let res = window_sum;
	for (let i = k; i < nums.length; i++) {
		window_sum += nums[i] - nums[i - k];
		res = Math.max(window_sum, res);
	}

	return res / k;
};

console.log(findMaxAverage([1,12,-5,-6,50,3], 4));
