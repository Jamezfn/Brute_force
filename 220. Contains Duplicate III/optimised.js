/**
 * @param {number[]} nums
 * @param {number} indexDiff
 * @param {number} valueDiff
 * @return {boolean}
 */
var containsNearbyAlmostDuplicate = function(nums, indexDiff, valueDiff) {
	const buckets = {};

	const bucket_size = valueDiff + 1;

	for (const [i, num] of nums.entries()) {
		const bucket_id = Math.floor(num / bucket_size);
		
		if (bucket_id in buckets) { return true; }

		if ((bucket_id - 1) in buckets && Math.abs(num - buckets[bucket_id - 1]) <= valueDiff) {
			return true;
		}

		if ((bucket_id + 1) in buckets && Math.abs(num - buckets[bucket_id + 1]) <= valueDiff) {
                        return true;
                }

		buckets[bucket_id] = num;
		if (i>=indexDiff) {
                        const old_bucket = Math.floor(nums[i - indexDiff] / bucket_size);
                        delete buckets[old_bucket];
                }

	}

	return false;
};

console.log(
    containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0)
);

console.log(
    containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3)
);

console.log(
    containsNearbyAlmostDuplicate([1, 2, 3, 1], 1, 2)
);
