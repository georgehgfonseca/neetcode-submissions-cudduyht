import heapq
from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.heap = []
        self.timestamp = 0
        self.numCount = defaultdict(int)

    def push(self, val: int) -> None:
        self.timestamp += 1
        self.numCount[val] += 1
        heapq.heappush(self.heap, (-self.numCount[val], -self.timestamp, val))

    def pop(self) -> int:
        (_, _, val) = heapq.heappop(self.heap)
        self.numCount[val] -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()