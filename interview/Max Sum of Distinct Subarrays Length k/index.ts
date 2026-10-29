function maxSum(nums: number[], k: number): number {
	let max_sum: number = -Infinity;
	let curr_sum: number = 0;
	let state: Map<number, number> = new Map();
	let start: number = 0;

	for (let end = 0; end < nums.length; end++) {
		curr_sum += nums[end];
		state.set(nums[end], (state.get(nums[end]) || 0) + 1);

		if (end - start + 1 === k) {
			if (state.size === k) {
				max_sum = Math.max(max_sum, curr_sum);
			}

			curr_sum -= nums[start];
			state.set(nums[start], state.get(nums[start])! - 1);
			if (state.get(nums[start]) === 0) {
				state.delete(nums[start]);
			}
			start++;
		}
	}

	return max_sum === -Infinity ? 0 : max_sum;
}


console.log(maxSum([3, 2, 2, 3, 4, 6, 7, 7, -1], 4));
