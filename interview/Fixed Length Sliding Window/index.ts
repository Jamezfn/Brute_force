function maxSubarraySum(nums: number[], k: number): number {
    let maxSum: number = -Infinity;
    let windowSum: number = 0;
    let start: number = 0;

    for (let end = 0; end < nums.length; end++) {
	    windowSum += nums[end];

	    if (end - start + 1 === k) {
		    maxSum = Math.max(maxSum, windowSum);
		    windowSum -= nums[start];
		    start++;
	    }
    }

    return maxSum;
}

console.log(maxSubarraySum([2, 1, 5, 1, 3, 2], 3));
