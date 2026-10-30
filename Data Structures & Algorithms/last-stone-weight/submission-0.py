import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            if len(stones) >= 2:
                largest1 = heapq.heappop_max(stones)
                largest2 = heapq.heappop_max(stones)
                diff = largest1 - largest2

                if diff == 0:
                    continue
                
                heapq.heappush_max(stones, diff)

        if stones:
            return stones[0]
        return 0
        