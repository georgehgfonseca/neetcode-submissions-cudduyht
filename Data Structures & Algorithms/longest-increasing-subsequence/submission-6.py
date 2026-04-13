from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # [0,3,1,3,2,3]
        # dfs(0, -1)
        #   dfs(1, -1)
        #   dfs(1, 0)

        @cache
        def dfs(i, j):
            if i == len(nums):
                return 0

            curr = dfs(i + 1, j) # not include

            if j == -1 or nums[j] < nums[i]:
                curr = max(curr, 1 + dfs(i + 1, i)) # include

            return curr

        return dfs(0, -1)

        