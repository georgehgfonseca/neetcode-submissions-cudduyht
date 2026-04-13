class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0] 
        for left in range(len(nums)):
            curr = 0
            for right in range(left, len(nums)):
                curr += nums[right]
                res = max(res, curr)
        return res
