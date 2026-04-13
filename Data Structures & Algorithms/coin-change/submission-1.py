class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins.sort()
        dp = dict()

        def dfs(target):
            if target == 0:
                return 0
            if target in dp:
                return dp[target]
            
            res = float("inf")
            for coin in coins:
                if target - coin < 0:
                    break
                res = min(res, 1 + dfs(target - coin))
            dp[target] = res
            return res
        
        res = dfs(amount)
        if res == float("inf"):
            return -1
        return res
        