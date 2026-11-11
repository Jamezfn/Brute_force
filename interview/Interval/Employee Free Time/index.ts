
function employeeFreeTime(schedule: number[][][]): number[][] {
	const flattened: number[][] = schedule.flat();
	flattened.sort((a, b) => a[0] - b[0]);

	const merged: number[][] = [];
	for (const interval of flattened) {
		if (merged.length === 0 || merged[merged.length - 1][1] < interval[0]) {
			merged.push(interval);
		} else {
			merged[merged.length - 1][1] = Math.max(merged[merged.length - 1][1], interval[1]);
		}
	}

	const free_time: number[][] = [];
	for (let i = 1; i < merged.length; i++) {
		let start: number = merged[i - 1][1];
		let end: number = merged[i][0];

		if (start < end) {
			free_time.push([start, end]);
		}
	}

	return free_time;
}


console.log(employeeFreeTime([[[2,4],[7,10]],[[1,5]],[[6,9]]]));