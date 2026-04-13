class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # at each level a decision - add another element of i-th index, or move to the next
        # dp reuse calculatation if at same currSum and i
        dp = dict()
        def dfs(currSum):
            if currSum in dp:
                return dp[currSum]
            if currSum > target:
                return 0
            if currSum == target:
                return 1
            res = 0
            for num in nums:
                dp[currSum + num] = dfs(currSum + num)
                res += dp[currSum + num]
            return res

        return dfs(0)

    def combinationSum42(self, nums: List[int], target: int) -> int:
        # at each level a decision - add another element of i-th index, or move to the next
        # dp reuse calculatation if at same currSum and i
        def dfs(i, currSum):
            print(i, currSum)
            if i >= len(nums) or currSum > target:
                print("returned 0")
                return 0
            if currSum == target:
                print("returned 1")
                return 1
            if i == len(nums) - 1:
                return dfs(i, currSum + nums[i])
            return dfs(i, currSum + nums[i]) + dfs(i + 1, currSum)
        return dfs(0, 0)