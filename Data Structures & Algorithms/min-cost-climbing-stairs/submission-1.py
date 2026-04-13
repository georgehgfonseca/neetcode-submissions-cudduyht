class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # calculate and store minimum cost to get to step x
        dp = [0, 0]

        for i in range(2, len(cost) + 1):
            dp.append(min(dp[-1] + cost[i - 1], dp[-2] + cost[i - 2]))
        
        return dp[-1]
        