
function nextGreaterElement(nums: number[]): number[] {
	const n = nums.length;
	const stack: number[] = [];
	const result: number[] = new Array(n).fill(-1);

	for (let i = 0; i < n; i++) {
		while (stack.length > 0 && nums[i] > nums[stack[stack.length - 1]]) {
			let index: number = stack.pop() as number;
			result[index] = nums[i];
		}
		stack.push(i);
	}

	return result;
}

console.log(nextGreaterElement([102, 101, 103, 102, 104, 103]));