/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSlidingWindow = function(nums, k) {
	const dq = [];
	const result = [];

	for (let i = 0; i < nums.length; i++) {
		while (dq.length && dq[0] < i - k) {
			dq.shift();
		}
		while (dq.length && nums[dq[dq.length - 1]] < nums[i]) {
			dq.pop();
		}

		dq.push(i);

		if (i >= k - 1) {
			result.push(nums[dq[0]]);
		}
	}

	return result;
};

console.log(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3));
console.log(maxSlidingWindow([1], 1));
