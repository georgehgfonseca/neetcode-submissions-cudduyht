from collections import deque
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # keep the max value and index
        # when a larger number is read, update it and discard the numbers to the left 
        # nums          = [1, 2, 1, 0, 4, 2, 6]
        #                             |       |
        #               = 6 
        # heap          = []
        # currNum       = 6
        # currMax       = -6
        # currIdx       = 6
        # res           = [-2, -2, -4, -4, -6]
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        r = k
        (currMax, currIdx) = heapq.heappop(heap)
        res = [-currMax]

        while r < len(nums):
            currNum = nums[r]
            if currNum >= currMax * -1:
                (currMax, currIdx) = -currNum, r
                heap = []
            else:
                heapq.heappush(heap, (-nums[r], r))
                while currIdx <= r - k:
                    (currMax, currIdx) = heapq.heappop(heap)
            res.append(-currMax)
            r += 1
        return res

        