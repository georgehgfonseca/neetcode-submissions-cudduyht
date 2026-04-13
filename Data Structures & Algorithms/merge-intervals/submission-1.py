class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        currStart, currEnd = intervals[0]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start <= currEnd:
                # merge
                currEnd = max(currEnd, end)
            else:
                res.append([currStart, currEnd])
                currStart, currEnd = start, end

        res.append([currStart, currEnd])        
        return res

            
        