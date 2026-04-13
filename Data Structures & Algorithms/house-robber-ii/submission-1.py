class Solution:
    def rob(self, nums: List[int]) -> int:

        def aux(nums):
            dp = [nums[0], max(nums[0], nums[1])]

            for i in range(2, len(nums)):
                dp.append(max(dp[-2] + nums[i], dp[-1]))

            return dp[-1]
        
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        return max(aux(nums[1:]), aux(nums[:-1]))
        
        