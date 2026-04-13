class Solution:
    def rob(self, nums: List[int]) -> int:
        # houses:     0 1 2 3
        # nums:       1 1 3 3
        # maxAtHouse: 1 1 4 4
        # max[i] = max(money[i - 2] + money[i], money[i - 1])
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        dp = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            dp.append(max(dp[-2] + nums[i], dp[-1]))
        
        return dp[-1]