class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # currMin currMax
        # nums             = [1, 2, -3, 4, -2]
        # currMax          = 2
        # currMin          = 2
        ans = nums[0]
        currMax = nums[0]
        currMin = nums[0]
        for i in range(1, len(nums)):
            tempMax = currMax * nums[i]
            tempMin = currMin * nums[i]
            currMax = max(nums[i], tempMax, tempMin)
            currMin = min(nums[i], tempMax, tempMin)
            ans = max(ans, currMax)
        return ans


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
            dp.pop(k)
        return ans