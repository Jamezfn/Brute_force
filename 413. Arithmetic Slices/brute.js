/**
 * @param {number[]} nums
 * @return {number}
 */
var numberOfArithmeticSlices = function(nums) {
	n = nums.length
	if (n < 3) { return 0; }
	let count = 0;
	for (let i = 0; i < n; i++) {
		for (let j = i + 2; j < n; j++) {
			const dif = nums[i + 1] - nums[i];
			const ari = true;

			for (let k = i + 1; k < j; k++) {
				if (nums[k + 1] - nums[k]  !== dif) {
					ari = false;
					break;
				}
			}

			if (ari) count +=1;
		}
	}

	return count;
};

console.log(numberOfArithmeticSlices([1,2,3,4]));
console.log(numberOfArithmeticSlices([7,7,7,7]));
console.log(numberOfArithmeticSlices([1,3,5,7,9]));
console.log(numberOfArithmeticSlices([1]));
