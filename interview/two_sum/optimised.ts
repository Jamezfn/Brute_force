function twoSum(nums: number[], target: int): boolean {
    let [l, r] = [0, nums.length - 1];

    while (l < r) {
	    let tt = nums[l] + nums[r];
	    if (tt === target) return true;

	    if (tt < target) {
		    l += 1;
	    } else {
		    r -= 1;
	    }
    }

    return false;
};


console.log(twoSum([1,3,4,6,8,10,13], 13))
