class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2

        dp = [[None] * (target + 1) for _ in range(len(nums) + 1)]

        self.found = False
        def dfs(i, currTarget):
            if currTarget == 0:
                self.found = True
                return True
            if i >= len(nums) or currTarget < 0:
                return False
            if dp[i][currTarget] != None:
                return dp[i][currTarget]
            
            dp[i][target] = dfs(i + 1, currTarget - nums[i]) or dfs(i + 1, currTarget)
            return dp[i][target]
        
        return dfs(0, target)
            
            
















    def canPartition2(self, nums: List[int]) -> bool:
        overallSum = sum(nums)
        self.canSplit = False
        def dfs(i, set1, set1Sum, set2, set2Sum):
            # prune search tree
            if set1Sum > overallSum / 2 or set2Sum > overallSum / 2:
                return
            if i >= len(nums):
                if set1Sum == set2Sum:
                    self.canSplit = True
                return
            set1.append(nums[i])
            dfs(i + 1, set1, set1Sum + nums[i], set2, set2Sum)
            set1.pop()
            
            set2.append(nums[i])
            dfs(i + 1, set1, set1Sum, set2, set2Sum + nums[i])
            set2.pop()
        
        dfs(0, [], 0, [], 0)
        return self.canSplit