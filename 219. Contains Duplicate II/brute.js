/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
	const n = nums.length;

	for (let i = 0; i < n; i++) {
		for (let j = i + 1; j < n; j++) {
			if (nums[i] === nums[j] && Math.abs(i - j) <= k) {
				return true;
			}
		}
	}

	return false;
};

console.log(containsNearbyDuplicate([1,2,3,1], k=3));
console.log(containsNearbyDuplicate([1,0,1,1], k=1));
console.log(containsNearbyDuplicate([1,2,3,1,2,3], k=2));
