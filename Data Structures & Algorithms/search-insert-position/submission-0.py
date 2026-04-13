class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search
        # target   = -2
        # nums     = [-1,0,2,4,6,8]
        # l        = 0
        # m        = 0
        # r        = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (r + l) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target: # search left
                r = m - 1
            else: # search right
                l = m + 1
        return l