class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        cost_benefit = [profits[i] / capital[i] if capital[i] != 0 else float("inf") for i in range(len(profits))]
        used = [False for _ in range(len(profits))]
        # profits   = [20, 24]
        # capital   = [9, 12]
        # w         = 12
        res = w
        for _ in range(k):
            # at each iteration, get the most profitable project within the capital
            maxIdx = -1
            maxProfit = -1
            for i in range(len(profits)):
                if not used[i] and capital[i] <= res and profits[i] > maxProfit:
                    maxProfit = profits[i]
                    maxIdx = i
            if maxIdx == -1:
                return res
            res += maxProfit
            print(maxIdx, maxProfit)
            used[maxIdx] = True
        return res
            
