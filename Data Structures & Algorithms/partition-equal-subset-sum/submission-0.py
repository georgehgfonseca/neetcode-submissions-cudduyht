class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        self.canSplit = False
        def dfs(i, set1, set1Sum, set2, set2Sum):
            if i >= len(nums):
                if set1Sum == set2Sum:
                    self.canSplit = True
                return
            dfs(i + 1, set1.copy() + [nums[i]], set1Sum + nums[i], set2, set2Sum)
            dfs(i + 1, set1, set1Sum, set2.copy() + [nums[i]], set2Sum + nums[i])

        
        dfs(0, [], 0, [], 0)
        return self.canSplit

        