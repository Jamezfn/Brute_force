function trappingWater(heights: number[]): number {
    if (!heights.length) return 0;

    let [l, r] = [0, heights.length - 1];
    let [lmax, rmax] = [heights[l], heights[r]];

    let count = 0;

    while (l < r) {
	    if (lmax < rmax) {
		    l++;
		    if (heights[l] >= lmax) {
			    lmax = heights[l];

		    } else {
			    count += lmax - heights[l];
		    }
	    } else {
		    r--;
		    if (heights[r] > rmax) {
			    rmax = heights[r];
		    } else {
			    count += rmax - heights[r]
		    } 
	    }
    }

    return count;
}

console.log(trappingWater([3, 4, 1, 2, 2, 5, 1, 0, 2]));
