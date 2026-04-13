from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)

        @cache
        def dfs(target):
            if target < 0:
                return float("inf")
            if target == 0:
                return 0
            
            best = float("inf")
            for coin in coins:
                best = min(best, 1 + dfs(target - coin))
            return best
        
        res = dfs(amount)

        return -1 if res == float("inf") else res
            


    def coinChange2(self, coins: List[int], amount: int) -> int:
        # dp with dfs including one coin per tree level
        # sort the coins for sligth perfomrance improvement (try larger 1st)
        coins.sort(reverse=True)
        self.res = float("inf")

        @cache
        def dfs(currSum, coinCount):
            if currSum > amount:
                return
            if currSum == amount:
                self.res = min(self.res, coinCount)
                return
            
            for coin in coins:
                dfs(currSum + coin, coinCount + 1)

        dfs(0, 0)
        
        if self.res == float("inf"):
            return -1
        return self.res
