function numSubarraysWithSum(nums: number[], goal: number): number {
	const len = nums.length;
	let ans = 0;
	for (let i = 0; i < len; i++) {
		let sum = 0;
		for (let j = i; j < len; j++) {
			sum += nums[i];

			if (sum > goal) {
				break;
			}

			if (sum === goal) {
				ans++;
			}
		}
	}

	return ans;
};

console.log(numSubarraysWithSum([1,0,1,0,1], 2));
