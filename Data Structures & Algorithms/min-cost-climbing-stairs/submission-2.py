class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        costStep = [cost[0], cost[1]]
        for step in range(2, len(cost) + 1):
            if step == len(cost):
                costStep.append(min(costStep[-2], costStep[-1]))
                break
            costStep.append(min(costStep[-2], costStep[-1]) + cost[step])
        return costStep[-1]

        