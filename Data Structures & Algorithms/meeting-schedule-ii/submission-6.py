"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort by starting time
        # keep track of ending times in a heapq
        intervals.sort(key=lambda x: x.start)
        unfinished_meetings = []
        res = 0

        for interval in intervals:
            start, end = interval.start, interval.end
            heapq.heappush(unfinished_meetings, end)
            while unfinished_meetings and unfinished_meetings[0] <= start:
                heapq.heappop(unfinished_meetings)
            
            res = max(res, len(unfinished_meetings))
        
        return res


        