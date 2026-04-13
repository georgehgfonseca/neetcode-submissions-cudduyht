class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        ans = []
        def helper(currIdx, currSum, currComb):
            # [2, 5, 6, 9]
            # cases:
            # not increase currIdx: helper(0, 2, [2])
            #     not increase currIdx: helper(0, 4, [2, 2])
            #     increase currIdx: helper(1, 2, [2,])
            # increase currIdx: helper(1, 0, [])
            #     not increase currIdx: helper(1, 5, [5])
            #     increase currIdx: helper(2, 0, [])
            if currSum == target:
                ans.append(currComb)
                return
            
            if currSum > target or currIdx >= len(nums):
                return

            helper(currIdx, currSum + nums[currIdx], currComb[:] + [nums[currIdx]])
            helper(currIdx + 1, currSum, currComb[:])

        helper(0, 0, [])
        return ans

            

        