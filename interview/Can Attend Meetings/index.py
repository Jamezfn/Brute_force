#!/usr/bin/env python

from typing import List

def canAttendMeetings(intervals: List[List[int]]) -> bool:
    if not intervals:
        return True

    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False

    return True

print(canAttendMeetings([(1,5),(3,9),(6,8)]))
