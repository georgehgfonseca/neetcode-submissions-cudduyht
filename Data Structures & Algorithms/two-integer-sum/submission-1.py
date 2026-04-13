class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementIndex = dict()
        for i, num in enumerate(nums):
            compl = target - num
            if compl not in complementIndex:
                complementIndex[compl] = i

        for i, num in enumerate(nums):
            if num in complementIndex:
                j = complementIndex[num]
                if j > i:   
                    return [i, j]
                if i > j:
                    return [j, i]