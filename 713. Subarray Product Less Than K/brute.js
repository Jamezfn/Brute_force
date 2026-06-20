"use strict";
function numSubarrayProductLessThanK(nums, k) {
    const n = nums.length;
    let count = 0;
    for (let i = 0; i < n; i++) {
        let product = 1;
        for (let j = i; j < n; j++) {
            product *= nums[j];
            if (product < k) {
                count++;
            }
        }
    }
    return count;
}
;
console.log(numSubarrayProductLessThanK([10, 5, 2, 6], 100));
console.log(numSubarrayProductLessThanK([1, 2, 3], 0));
