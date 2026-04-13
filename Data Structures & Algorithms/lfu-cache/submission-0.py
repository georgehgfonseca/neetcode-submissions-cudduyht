import heapq
#class ListNode:
#    def __init__(self, key, value)

class LFUCache:

    def __init__(self, capacity: int):
        self.heap = []
        self.map = dict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.map:
            self.map[key] = (self.map[key][0], self.map[key][1] + 1)
            print(f"Returned {key} = {self.map[key]}")
            return self.map[key][0]
        print(f"Returned -1")
        return -1

        

    def put(self, key: int, value: int) -> None:
        if len(self.map) >= self.capacity:
            # remove LFU
            # TODO: handle ties
            minFreq = float("inf")
            minKey = None
            for existing_key in self.map:
                if self.map[existing_key][1] < minFreq:
                    minFreq = self.map[existing_key][1]
                    minKey = existing_key
            print(f"Removed {minKey}")
            self.map.pop(minKey)

        if key not in self.map:
            self.map[key] = (value, 1)
        else:
            self.map[key] = (value, self.map[key][1] + 1)
        print(f"Added {key} = {self.map[key]}")
#        heapq.heappush(self.heap, (key, value))


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)