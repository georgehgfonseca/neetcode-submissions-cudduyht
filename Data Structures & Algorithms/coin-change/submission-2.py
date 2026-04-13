class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = {0: 0}
        def dfs(target):
            if target in dp:
                return dp[target]

            minCoins = float("inf")
            for coin in coins:
                if target - coin >= 0:
                    minCoins = min(minCoins, dfs(target - coin) + 1)
            dp[target] = minCoins
            return minCoins
        
        res = dfs(amount)
        if res == float("inf"):
            return -1
        return res

    def coinChange2(self, coins: List[int], amount: int) -> int:
        
        dp = {0: 0}
        def dfs(curr):
            if curr in dp:
                return dp[curr] 
            for coin in coins:
                if curr + coin <= amount:
                    # used one coin to go from curr to curr - coin
                    dp[curr + coin] = dp[curr] + 1
                    dfs()
                if curr + coin == amount:
                    break
        
        dfs(0)
        return dp[amount]