function insertIntervals(intervals: number[][], newInterval: number[]): number[][] {
    const merged: number[][] = [];
    const n: number = intervals.length;
    let i: number = 0;


    while (i < n && intervals[i][1] < newInterval[0]) {
	    merged.push(intervals[i]);
	    i++;
    }

    while (i < n && intervals[i][0] <= newInterval[1]) {
	    newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
	    newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
	    i++
    }

    merged.push(newInterval);

    for (let j = i; j < n; j++) {
	    merged.push(intervals[j])
    }

    return merged;
}

console.log(insertIntervals([[1,2],[3,5],[6,7],[8,10]], [5,6]));
