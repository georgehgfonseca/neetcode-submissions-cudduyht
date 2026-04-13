class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        minAppear = len(nums) // 3
        numCount = dict()
        for num in nums:
            numCount[num] = numCount.get(num, 0) + 1
        
        res = []
        for num in numCount:
            if numCount[num] > minAppear:
                res.append(num)
        return res
        