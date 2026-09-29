from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i == n:
                return 1
            if i > n:
                return 0

            oneStep = dfs(i + 1)
            twoSteps = dfs(i + 2)
            dp[i] = oneStep + twoSteps
            return dp[i]

        return dfs(0)
