class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {1: cost[0], 2: cost[1]}
        cost.append(0)
        for i in range(3, len(cost) + 1):
            dp[i] = cost[i - 1] + min(dp[i - 1], dp[i - 2])
        return dp[len(cost)]