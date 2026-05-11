/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSlidingWindow = function(nums, k) {
	const n = nums.length;
	const w = [];

	for (let i = 0; i < n; i++) {
		let max_v = nums[i];
		for (let j = i; j < k + i; j++) {
			if (nums[j] > max_v) { max_v = nums[j]; }
		}
		w.push(max_v);
	}

	return w;
};


console.log(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3));
console.log(maxSlidingWindow([1], 1));
