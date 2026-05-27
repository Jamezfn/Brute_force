/**
 * @param {number[]} nums
 * @return {number}
 */
var numberOfArithmeticSlices = function(nums) {
	const n = nums.length;

	if (n < 3) return 0

	let cur = 0;
	let total = 0;

	for (let i = 2; i < n; i++) {
		if (nums[i] - nums[i - 1] === nums[i - 1] - nums[i - 2]) {
			cur++;
			total += cur;
		} else {
			cur = 0;
		}
	}

	return total;
};

console.log(numberOfArithmeticSlices([1,2,3,4]));
console.log(numberOfArithmeticSlices([7,7,7,7]));
console.log(numberOfArithmeticSlices([1,3,5,7,9]));
console.log(numberOfArithmeticSlices([1]));
