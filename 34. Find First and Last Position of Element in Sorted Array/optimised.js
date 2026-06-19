"use strict";
function binary(nums, target, first) {
    let [l, r] = [0, nums.length - 1];
    let i = -1;
    while (l <= r) {
        let mid = Math.floor((l + r) / 2);
        if (target > nums[mid]) {
            l = mid + 1;
        }
        else if (target < nums[mid]) {
            r = mid - 1;
        }
        else {
            i = mid;
            if (first) {
                r = mid - 1;
            }
            else {
                l = mid + 1;
            }
        }
    }
    return i;
}
function searchRange(nums, target) {
    return [binary(nums, target, true), binary(nums, target, false)];
}
;
console.log(searchRange([5, 7, 7, 8, 8, 10], 8));
