function canAttendMeetings(intervals: number[][]): boolean {
	if (intervals.length === 0) {
		return true;
	}

	intervals.sort((a, b) => a[0] - b[0]);

	for (let i = 1; i < intervals.length; i++) {
		if (intervals[i][0] < intervals[i - 1][1]) {
			return false;
		}
	}

	return true;
}

console.log(canAttendMeetings([[1, 5], [3, 9], [6, 8]]));
