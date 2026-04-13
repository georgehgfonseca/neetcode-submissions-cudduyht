class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # nums        = [-1,-2,1]
        # i           =        *
        # curr        = -1
        # res         = -1
        res = nums[0]
        curr = res

        for i in range(1, len(nums)):
            if curr < 0 and nums[i] < 0:
                res = max(res, curr, nums[i])
                continue
            if curr < 0:
                curr = 0
            curr += nums[i]
            res = max(curr, res)

        return res
