function trap(height: number[]): number {
	const n = height.length;

	let water = 0;
	for (let i = 0; i < n; i++) {
		let left_max = 0;
		let right_max = 0;


		for (let l = 0; l < i; l++) {
			left_max = Math.max(left_max, height[l]);
		}

		for (let r = i; r < n; r++) {
                        right_max = Math.max(right_max, height[r]);
                }

		water += Math.max(Math.min(left_max, right_max) - height[i], 0); 
	}

	return water;
};

console.log(trap([0,1,0,2,1,0,1,3,2,1,2,1]));
console.log(trap([4,2,0,3,2,5]));
