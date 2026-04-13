class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers
        # prices       = [7, 1, 5, 3, 6, 4]
        # l, r         =     l  r
        l, r = 0, 1
        ans = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                ans += prices[r] - prices[l]
            l += 1
            r += 1
        return ans