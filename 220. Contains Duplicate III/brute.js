/**
 * @param {number[]} nums
 * @param {number} indexDiff
 * @param {number} valueDiff
 * @return {boolean}
 */
var containsNearbyAlmostDuplicate = function(nums, indexDiff, valueDiff) {
	const n = nums.length;

	for (let i = 0; i < n; i++) {
		for (let j = i + 1; j < Math.min(i + indexDiff + 1, n); j++) {
			if (Math.abs(nums[i] - nums[j]) <= valueDiff) {
				return true;
			}
		}
	}

	return false;
};


console.log(containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0));

console.log(containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3));
