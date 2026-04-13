class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n * k)
        # use a hashmap to count occurencies
        numCount = dict()
        for num in nums:
            numCount[num] = numCount.get(num, 0) + 1
        
        # then iterate k times over the hashmap's keys to get the k-th most frequente element
        # [3, 0, 1, 0]
        # {3: 1, 0: 2, 1: 1}
        ans = []
        for _ in range(k):
            currMax = None
            maxCount = 0
            for num in numCount:
                if numCount[num] > maxCount:
                    currMax = num
                    maxCount = numCount[num]
            if currMax == None:
                raise Exception("Could not count the k-th most frequent element")
            ans.append(currMax)
            numCount.pop(currMax)
        return ans

        