"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort the meetings by start time
        intervals.sort(key=lambda x: x.start)
        # heap of unfinished meeting
        unfinished = []
        res = 0
        for interval in intervals:
            # remove meetings that finished at interval.start
            while unfinished and unfinished[0] <= interval.start:
                heapq.heappop(unfinished)

            heapq.heappush(unfinished, interval.end)
            # monitor the heap size throughtout the execution
            res = max(res, len(unfinished))
        
        return res
