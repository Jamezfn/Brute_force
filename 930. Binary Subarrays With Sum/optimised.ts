function numSubarraysWithSum(nums: number[], goal: number): number {
	function atMost(x) {
		const len = nums.length;
		let tt = 0;
		let ans = 0;
		let i = 0;
		for (let j = 0; j < len; j++) {
			tt += nums[j];

			while (tt > x) {
				tt -= nums[i];
				i++;
			}

			ans += j - i + 1;
		}

		return ans
	}

	return atMost(goal) - atMost(goal - 1);
};

console.log(numSubarraysWithSum([1,0,1,0,1], 2))
