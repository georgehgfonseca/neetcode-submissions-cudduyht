class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #          [3, 4, 5, 6]
        #          {4: 0}
        # i      = 1
        # target = 7
        complementIdxs = dict()
        for i in range(len(nums)):
            if nums[i] in complementIdxs:
                if i < complementIdxs[nums[i]]:
                    return [i, complementIdxs[nums[i]]]
                return [complementIdxs[nums[i]], i]
            complement = target - nums[i]
            complementIdxs[complement] = i

        