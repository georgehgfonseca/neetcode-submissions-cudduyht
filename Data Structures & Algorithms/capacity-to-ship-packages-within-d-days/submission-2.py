class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # at least the largest weight
        # at most ceil(len(weights) / days) * largest weight
        # binary search within these bounds
        # n     = [1,5,4,4,2,3]
        # days  = 3
        # try to fit packages together based on the largest weight
        # from largest, try to add smallest, move pointers when not possible
        def canFit(weights, days, cap):
            matchCount = 0
            setCount = 0
            currWeight = 0
            i = 0
            while i < len(weights):
                setCount += 1
                currWeight = weights[i]
                while i + 1 < len(weights) and currWeight + weights[i + 1] <= cap:
                    currWeight += weights[i + 1]
                    i += 1

                i += 1

            return setCount <= days

        lowerBound = max(weights)
        if len(weights) <= days:
            return lowerBound

        upperBound = math.ceil(len(weights) / days) * lowerBound

        l, r = lowerBound, upperBound
        while l <= r:
            m = (l + r) // 2
            if canFit(weights, days, m):
                r = m - 1
            else:
                l = m + 1
        
        return l 