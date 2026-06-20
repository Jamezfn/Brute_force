"use strict";
function numSubarrayProductLessThanK(nums, k) {
    const n = nums.length;
    let count = 0;
    let product = 1;
    let i = 0;
    for (let j = 0; j < n; j++) {
        product *= nums[j];
        while (product >= k) {
            product = Math.floor(product / nums[j]);
        }
        count += j - i + 1;
    }
    return count;
}
;
console.log(numSubarrayProductLessThanK([10, 5, 2, 6], 100));
console.log(numSubarrayProductLessThanK([1, 2, 3], 0));
