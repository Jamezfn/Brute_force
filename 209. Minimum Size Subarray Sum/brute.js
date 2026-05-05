/**
 * @param { number } target
 * @param { number[] } nums
 * @return { number }
 */

var minSubArrayLen = function(target, nums) {
	const n = nums.length;
	let ans = Infinity;

	for (let i = 0; i <= n; i++) {
		let total = 0;
		for (let j = i; j <= n; j++) {
			total += nums[j];
			if (total >= target) {
				ans = Math.min(ans, j - i + 1);
				break;
			}
		}
	}

	return ans === Infinity ? 0 : ans;
};


console.log(minSubArrayLen(4, [2,3,1,2,4,3]));
