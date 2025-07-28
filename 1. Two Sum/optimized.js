#!/usr/bin/env node
/**
 * @param {number[]} nums
 * @param {number} target
 * @param {number[]}
 */

var twoSum = function(nums, target) {
	const seen = new Map();
	for (let i = 0; i < nums.length; i++) {
		const dif = target - nums[i];
		if (seen.has(dif)) {
			return [seen.get(dif), i];
		}
		seen.set(nums[i], i);
	}
};

console.log(twoSum([2, 7, 11, 15], 9));
console.log(twoSum([3, 2, 4], 6));
console.log(twoSum([3, 3], 6));
