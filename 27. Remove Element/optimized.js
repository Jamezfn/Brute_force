#!/usr/bin/env node
/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
	let k = 0;
	for (let i = 0; i < nums.length; i++) {
		if (nums[i] !== val) {
			nums[k++] = nums[i];
		}
	}
	return k;
};

let arr1 = [3,2,2,3]
k1 = removeElement(arr1, 3)
console.log(k1, arr1.slice(0, k1))

let arr2 = [0,1,2,2,3,0,4,2]
k2 = removeElement(arr2, 2)
console.log(k2, arr2.slice(0, k2))
