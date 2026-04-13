"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) < 2:
            return True
        intervals.sort(key=lambda x: x.start)
        lastEnd = intervals[0].end
        for i in range(1, len(intervals)):
            if intervals[i].start < lastEnd:
                return False
            lastEnd = intervals[i].end
        return True
