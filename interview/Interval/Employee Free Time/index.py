#!/usr/bin/env python

from typing import List

def employeeFreeTime(schedule: List[List[List[int]]]) -> List[List[int]]:
    flattened = [interval for intervals in schedule for interval in intervals]
    flattened.sort(key=lambda x: x[0])

    merged = []
    for interval in flattened:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[0])
    
    free_times = []
    for i in range(1, len(merged)):
        start = merged[i - 1][1]
        end = merged[i][0]

        if end > start:
            free_times.append([start, end])

    return free_times

print(employeeFreeTime([[[2,4],[7,10]],[[1,5]],[[6,9]]]))
