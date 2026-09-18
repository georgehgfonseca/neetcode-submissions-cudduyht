class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = prices[0]
        for i in range(len(prices)):
            if prices[i] > lowest:
                profit = max(profit, prices[i] - lowest)
            else:
                lowest = prices[i]

        return profit
