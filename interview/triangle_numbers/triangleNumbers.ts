
function triangleNumber(nums: number[]): number {
    nums.sort((a, b) => a - b);

    let count = 0;

    for (let i = nums.length - 1; i > 1; i--) {
	    let l = 0;
	    let r = i - 1;

	    while (l < r) {
		    if (nums[l] + nums[r] > nums[i]) {
			    count += r - l;
			    r -= 1;
		    } else {
			    l += 1
		    }
	    }
    }

    return count;
}

console.log(triangleNumber([11,4,9,6,15,18]))
