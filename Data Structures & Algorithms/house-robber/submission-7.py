from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        @cache
        def dfs(i, robbed):
            if i >= n:
                return 0

            if robbed:
                return nums[i] + dfs(i + 1, False)
                        
            return max(dfs(i + 1, False), dfs(i + 1, True))
        
        return max(dfs(0, True), dfs(0, False))
