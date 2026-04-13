class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # brute force would be O(n^3)
        # dynamic programming by array size starting from 2 (i, j): product
        ans = max(nums)
        dp = {2: dict()}
        for i in range(len(nums) - 1):
            dp[2][(i, i + 1)] = nums[i] * nums[i + 1]
            ans = max(ans, dp[2][(i, i + 1)])
        
        for k in range(2, len(nums)):
            # compute the product of each subarray of size i + 1 using the subarrrays of size i
            dp[k + 1] = dict()
            for (i, j) in dp[k]:
                if j + 1 < len(nums):
                    dp[k + 1][(i, j + 1)] = dp[k][(i, j)] * nums[j + 1]
                    ans = max(ans, dp[k + 1][(i, j + 1)])
                if i - 1 > 0:
                    dp[k + 1][(i - 1, j)] = dp[k][(i, j)] * nums[i - 1]
                    ans = max(ans, dp[k + 1][(i - 1, j)])

        return ans