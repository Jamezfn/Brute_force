nums = [2,0,4,0,9];

function moveZeroes(nums: number[]): void {
    let i = 0;
    for (let j = 0; j < nums.length; j++) {
	    if (nums[j] !== 0) {
		    [nums[i], nums[j]] = [nums[j], nums[i]];
		    i++;
	    }
    }
}
console.log(nums);

moveZeroes(nums);

console.log(nums);
