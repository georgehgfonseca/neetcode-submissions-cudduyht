class Solution:
    def rob(self, nums: List[int]) -> int:
        # run starting by 0-th index and by the 1-th index
        if len(nums) == 1:
            return nums[0]

        dpEven = {0: nums[0], 1: max(nums[0], nums[1])}
        for i in range(2, len(nums) - 1):
            dpEven[i] = max(dpEven[i - 1], dpEven[i - 2] + nums[i])
        dpOdd = {0: 0, 1: nums[1]}
        for i in range(2, len(nums)):
            dpOdd[i] = max(dpOdd[i - 1], dpOdd[i - 2] + nums[i])
        
        return max(dpEven[len(nums) - 2], dpOdd[len(nums) - 1])