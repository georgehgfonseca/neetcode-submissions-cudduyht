class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals     = [[1,2], [3,5], [6,10]]
        # i             =                  *
        # new           = [6,10]
        # res           = [[1,2]]
        newStart, newEnd = newInterval
        res = []
        for i in range(len(intervals)):
            start, end = intervals[i]
            if newStart > end:
                res.append(intervals[i])
                continue
            
            if newEnd < start:
                res.append([newStart, newEnd])
                res += intervals[i:]
                return res

            newStart = min(newStart, start)
            newEnd = max(newEnd, end)
        
        res.append([newStart, newEnd])
        
        return res

        