class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums = [-1,0,2,4,6,8]
        # l = 3
        # r = 3
        # m = 4
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (r + l) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1
        