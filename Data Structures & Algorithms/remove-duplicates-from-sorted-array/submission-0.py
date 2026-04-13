class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # swap dupliccates with postions after len(nums)
        # brute force - iterate each index and rearrange if duplicated
        # if I find a dupliccate shift r pointed uuntil a new element is fouund
        # nums         = [1, 2, 3, 4, 4]
        # l            = 3
        # r            = 5
        l, r = 0, 1
        while r < len(nums):
            while nums[l] == nums[r]:
                r += 1
                if r >= len(nums):
                    return l + 1
            l += 1
            nums[l] = nums[r]
        return l + 1



        