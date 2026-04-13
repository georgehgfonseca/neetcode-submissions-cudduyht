class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort the intervals
        # int       = [[-100, -2], [1, 2], [2, 3], [5, 7]]
        # i         =     *
        # currEnd   = 4
        # res       = 1
        intervals.sort()
        currEnd = float("-inf")
        res = 0
        for i in range(len(intervals)):
            if intervals[i][0] >= currEnd:
                currEnd = intervals[i][1]
            else:
                res += 1
                currEnd = min(currEnd, intervals[i][1])
        
        return res

        