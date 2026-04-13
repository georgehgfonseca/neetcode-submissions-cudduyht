class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use the array as the hash-set
        # iterate over the nums with i
        # mark the i-th postion as negative, indicating that it has been seen
        # when reading a negative position, return the index as response
        # nums       = [-1, -3, -4, -2, 2]
        # i          = 4
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                return abs(nums[i])
            nums[abs(nums[i]) - 1] *= -1
        