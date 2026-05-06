/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
	const w = new Set();

	for (const [i, num] of nums.entries()) {
		if (w.has(num)) {
			return true;
		}
		w.add(num);
		if (w.size > k) {
			w.delete(nums[i - k]);
		}
	}

	return false;
};

console.log(containsNearbyDuplicate([1,2,3,1], k=3));
console.log(containsNearbyDuplicate([1,0,1,1], k=1));
console.log(containsNearbyDuplicate([1,2,3,1,2,3], k=2));
