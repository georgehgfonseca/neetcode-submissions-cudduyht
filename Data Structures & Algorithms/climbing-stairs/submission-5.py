from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        # brute force
        @cache
        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0

            oneStep = dfs(i + 1)
            twoSteps = dfs(i + 2)
            return oneStep + twoSteps

        return dfs(0)
        