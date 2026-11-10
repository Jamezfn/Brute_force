function nonOverlappingIntervals(intervals: number[][]): number {
	if (intervals.length === 0) {
		return 0;
	}

	let count: number = 1;
	let end: number = intervals[0][1];

	for (let i = 1; i < intervals.length; i++) {
		if (intervals[i][0] >= end) {
			end = intervals[i][1];
			count++;
		}
	}

	return intervals.length - count;
}

console.log(nonOverlappingIntervals([[1,3],[5,8],[4,10],[11,13]]));