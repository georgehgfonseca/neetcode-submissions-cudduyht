class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums            = [5,5,1,1,1,5,5]
        # numOccurencies  = {5: 4, 1: 3} 
        # create a hashmap of num and occurencies
        numOccurencies = dict()
        for num in nums:
            numOccurencies[num] = numOccurencies.get(num, 0) + 1
        
        # iterate over the keys and return which ever element whose value is >= len(nuns) // 2
        for num in numOccurencies:
            if numOccurencies[num] >= len(nums) // 2:
                return num
        