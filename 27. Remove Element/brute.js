#!/usr/bin/env node
/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
	let n = nums.length;
	for (let i = 0; i < n; i++) {
		if (nums[i] === val) {
			for (let j = i; j < n - 1; j++){
				nums[j] = nums[j+1];
			}
			n--;
			i--;
		}
	}
	return n;
};

let arr1 = [3,2,2,3]
k1 = removeElement(arr1, 3)
console.log(k1, arr1)

let arr2 = [0,1,2,2,3,0,4,2]
k2 = removeElement(arr2, 2)
console.log(k2, arr2)
