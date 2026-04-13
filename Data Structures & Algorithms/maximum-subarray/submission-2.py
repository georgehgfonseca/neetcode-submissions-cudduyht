class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # [2, -3, 4, -2, 2, 1, -1, 4]
        # maxSum  = 7
        # currSum = 7
        # i       = 6
        maxSum = nums[0]
        currSum = max(nums[0], 0)
        for i in range(1, len(nums)):
            currSum += nums[i]
            maxSum = max(maxSum, currSum)
            currSum = max(currSum, 0)
        return maxSum
        