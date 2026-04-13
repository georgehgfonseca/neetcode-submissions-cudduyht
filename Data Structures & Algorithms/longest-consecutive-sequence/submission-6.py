class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sort nums
        # tow pointers - whenever nums[i] == nums[i + 1] increase right pointer keep track of sizes
        # when != move left to right + 1
        # nums  = [2,3,4,4,5,10,20]
        # i     =  *
        nums = list(set(nums))
        if len(nums) == 1:
            return 1

        nums.sort()
        res = 0
        i = 0
        while i < len(nums) -1:
            curr = 1
            while i < len(nums) -1 and nums[i] + 1 == nums[i + 1]:
                curr += 1
                i += 1

            res = max(res, curr)
            i += 1

        return res
        