class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums          = [1, 0, 2, 2]
        # start2        = 2
        # i             = 2
        # follow up
        start2 = len(nums)
        end0 = -1
        i = 0
        while i < start2:
            if nums[i] == 0:
                # swap
                end0 += 1
                temp = nums[end0]
                nums[end0] = nums[i]
                nums[i] = temp
                # i -= 1
            if nums[i] == 2:
                # swap
                start2 -= 1
                temp = nums[start2]
                nums[start2] = nums[i]
                nums[i] = temp
                i -= 1
            i += 1

        return
        # move all 2s to the end, save first index with 2s
        # decrease i when a swap is made
        # when i == start2 break
        start2 = len(nums)
        i = 0
        while i < start2:
            if nums[i] == 2:
                # swap
                start2 -= 1
                temp = nums[start2]
                nums[start2] = nums[i]
                nums[i] = temp
                i -= 1
            i += 1
        
        # move all 1s to before the index where the 2s begin 
        start1 = start2
        i = 0
        while i < start1:
            if nums[i] == 1:
                # swap
                start1 -= 1
                temp = nums[start1]
                nums[start1] = nums[i]
                nums[i] = temp
                i -= 1
            i += 1


        