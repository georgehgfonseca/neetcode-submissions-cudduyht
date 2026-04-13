"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort the intervals
        # iterate over the intervals
        # group intervals when possible, marking as scheduled
        if len(intervals) < 2:
            return len(intervals)

        intervals.sort(key=lambda x:x.start)
        scheduled = [False for _ in intervals]
        ans = 0
        for i in range(len(intervals)):
            if scheduled[i]:
                continue
            scheduled[i] = True
            ans += 1
            lastEnd = intervals[i].end
            for j in range(i + 1, len(intervals)):
                if scheduled[j]:
                    continue
                if intervals[j].start >= lastEnd:
                    scheduled[j] = True
                    lastEnd = intervals[j].end
        return ans

