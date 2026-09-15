class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         complement = dict()
         for i in range(len(nums)):
            if nums[i] in complement:
                return [complement[nums[i]], i]
            diff = target - nums[i]
            complement[diff] = i