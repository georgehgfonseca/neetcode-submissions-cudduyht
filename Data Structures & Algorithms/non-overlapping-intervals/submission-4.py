class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort intervals
        # iterate, when a conflict is found, emove the one with latest end time (?)
        # intervals = [[0,2],[1,3],[2,4],[3,5],[4,6]]
        # curr_end  = 2

        intervals.sort()
        last_non_overlapping = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            start_time, end_time = intervals[i]

            if start_time >= last_non_overlapping:
                last_non_overlapping = end_time
                continue

            res += 1
            last_non_overlapping = min(last_non_overlapping, end_time)

        return res
