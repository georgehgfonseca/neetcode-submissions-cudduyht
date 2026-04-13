class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # backtracking - add one more of this idx or move to next idx
        # stop when currSum > target or idx >= len(nums)

        ans = []
        def helper(idx, currSum, currComb):
            if currSum == target:
                ans.append(currComb)
                return
            
            if currSum > target or idx >= len(nums):
                return

            helper(idx, currSum + nums[idx], currComb[:] + [nums[idx]])
            helper(idx + 1, currSum, currComb[:])
        
        helper(0, 0, [])
        return ans