class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numCount = defaultdict(int)
        threshold = len(nums) // 3
        for num in nums:
            numCount[num] += 1
        
        res = []
        for num in numCount:
            if numCount[num] > threshold:
                res.append(num)
        
        return res