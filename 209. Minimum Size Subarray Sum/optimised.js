/**
 * @param { number } target
 * @param { number[] } nums
 * @return { number }
 */

var minSubArrayLen = function(target, nums) {
	const n = nums.length;
	let left = 0;
	let total = 0;
	let ans = Infinity;

	for (let right = 0; right <= n; right++) {
		total += nums[right];

		while (total >= target) {
			ans = Math.min(ans, right - left + 1);
			total -= nums[left];
			left += 1;
		}
	}

	return ans === Infinity ? 0 : ans;
};

console.log(minSubArrayLen(4, [2,3,1,2,4,3]));
