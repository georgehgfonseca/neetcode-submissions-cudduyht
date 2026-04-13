class LinkedList:

    def __init__(self, val = 0, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        # dict to map each value to an index and node
        # always keep ref of the first and last nodes
        # when updating, move node to first
        self.cache = []
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                record = self.cache[i]
                self.cache.pop(i)
                self.cache.insert(0, record)
                return self.cache[0][1]
        return -1
        

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                record = (key, value)
                self.cache.pop(i)
                self.cache.insert(0, record)
                return

        self.cache.insert(0, (key, value))
        if len(self.cache) > self.capacity:
            self.cache.pop()
        


        
