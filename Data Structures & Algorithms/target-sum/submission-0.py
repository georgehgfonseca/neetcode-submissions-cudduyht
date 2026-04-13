class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dfs(i, sum):
            if i == len(nums):
                if sum == target:
                    return 1
                return 0

            return dfs(i + 1, sum + nums[i]) + dfs(i + 1, sum - nums[i])

        return dfs(0, 0)
            
