class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # nums         = [4, 2, 7, 6]
        # firstMissing = 3
        # iterate over nums
        # firstMissing = 3
        # store the i-th + 1 if larger than first missing
        # using O(n) space
        nums = set(nums)
        maxNum = max(nums)
        if maxNum < 1:
            return 1

        for i in range(1, maxNum + 2):
            if i not in nums:
                return i
