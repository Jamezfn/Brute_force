
function sortColors(nums: number[]): void {
    let [l, r] = [0, nums.length - 1];

    let i = 0;

    while (i <= r) {
	    if (nums[i] === 0) {
		    [nums[i], nums[l]] = [nums[l], nums[i]];
		    l++;
		    i++;
	    }
	    else if (nums[i] === 2) {
		    [nums[i], nums[r]] = [nums[r], nums[i]];
                    r--;
                    i++;
	    }
	    else {
		    i++;
	    }
    }
}

nums = [2,1,2,0,1,0,1,0,1];
console.log(nums);
sortColors(nums);
console.log(nums);
