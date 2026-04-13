import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit = []
        minCapital = [(capital[i], profits[i]) for i in range(len(capital))]
        heapq.heapify(minCapital)

        for _ in range(k):
            while minCapital and minCapital[0][0] <= w:
                (c, p) = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, (-p, c))

            if not maxProfit:
                break

            (p, c) = heapq.heappop(maxProfit)
            w += -p

        return w

        # profits   = [20, 24]
        # capital   = [9, 12]
        # w         = 12
        res = w
        profit_capital = [(profits[i], capital[i], False) for i in range(len(capital))]
        profit_capital.sort(reverse=True)
        for _ in range(k):
            # at each iteration, get the most profitable project within the capital
            maxIdx = -1
            for i in range(len(profit_capital)):
                if not profit_capital[i][2] and profit_capital[i][1] <= res:
                    res += profit_capital[i][0]
                    profit_capital[i] = (profit_capital[i][0], profit_capital[i][1], True)
                    maxIdx = i
                    break
            if maxIdx == -1:
                return res
        return res
            
