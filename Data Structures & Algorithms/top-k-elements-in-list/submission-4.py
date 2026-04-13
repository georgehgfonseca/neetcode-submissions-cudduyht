class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter, then convert to pairs, then sort
        freqs = Counter(nums)
        freqNum = [(freqs[num], num) for num in freqs]
        freqNum.sort(reverse=True)
        res = []
        for i in range(k):
            res.append(freqNum[i][1])
        return res