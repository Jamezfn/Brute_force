function max_area(heights: number[]) {
	let [left, right] = [0, heights.length - 1];

	let current_max = 0;
	while (left < right) {
		let width = right - left;
		let height = Math.min(heights[left], heights[right]);

		let current_area = width * height;

		current_max = Math.max(current_max, current_area);

		if (heights[left] < heights[right]) {
			left += 1;
		} else {
			right -= 1
		}
	}


	return current_max;
}


console.log(max_area([3, 4, 1, 2, 2, 4, 1, 3, 2]))
