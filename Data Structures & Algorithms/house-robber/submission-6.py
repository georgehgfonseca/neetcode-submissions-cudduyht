class Solution:
    def rob(self, nums: List[int]) -> int:
        # at dp[i] can rob previous (= dp[i -1]) or not (= dp[i - 2] + nums[i])
        if len(nums) == 1:
            return nums[0]
        dp = {0: nums[0], 1: max(nums[0], nums[1])}
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[len(nums) - 1]
        