"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        added_interval = [False for _ in intervals]
        res = []
        for i in range(len(intervals)):
            if not added_interval[i]:
                res.append([intervals[i]])
                for j in range(i + 1, len(intervals)):
                    lastest_interval = res[-1][-1]
                    if not added_interval[j] and lastest_interval.end <= intervals[j].start:
                        # can be scheduled together
                        res[-1].append(intervals[j])
                        added_interval[j] = True
        return len(res)
