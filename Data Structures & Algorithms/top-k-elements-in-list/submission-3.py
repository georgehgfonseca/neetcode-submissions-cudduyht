class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dict of nums and occurencies
        # dict of occurencies and nums
        # use a heap to get the top k occurencies
        numCount = Counter(nums)
        countNum = defaultdict(list)
        seenCounts = set()

        for num in numCount:
            seenCounts.add(numCount[num])
            countNum[numCount[num]].append(num)
        
        seenCountsHeap = []
        for count in seenCounts:
            heapq.heappush(seenCountsHeap, -count)
        
        res = []

        while len(res) < k:
            count = heapq.heappop(seenCountsHeap) * -1
            res += countNum[count]
        
        return res
        
        print(numCount)
        print(countNum)




        