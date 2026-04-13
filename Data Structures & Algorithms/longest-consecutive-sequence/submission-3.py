class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums   = [2,3,4,4,5,10,20]
        # i      =        *
        # start  =  *
        if len(nums) == 1:
            return 1
        nums.sort()
        i = 0
        res = 0
        while i < len(nums) - 1:
            start = i
            while nums[i] + 1 == nums[i + 1] or nums[i] == nums[i + 1]:
                if nums[i] == nums[i + 1]:
                    start += 1
                i += 1
                if i + 1 >= len(nums):
                    break
            i += 1
            res = max(res, i - start)
        return res