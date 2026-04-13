class ListNode:

    def __init__(self, key = 0, val = 0, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f"({self.key}, {self.val})"

class LRUCache:

    def __init__(self, capacity: int):
        # dict to map each value to an index and node
        # always keep ref of the first and last nodes
        # when updating, move node to first
        self.cache = dict()
        self.first = ListNode()
        self.last = ListNode()
        self.first.next = self.last
        self.last.prev = self.first
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.cache:
            if len(self.cache) == 1:
                return self.cache[key].val 
            
            node = self.cache[key]
            # 'remove' node from curr pos
            node.prev.next = node.next
            node.next.prev = node.prev

            # reinsert at beginning
            node.next = self.first.next
            node.prev = self.first
            self.first.next = node
            node.next.prev = node
            return self.cache[key].val

        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            # 'remove' node from curr pos
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            node = ListNode(key, value)

        node.next = self.first.next
        node.prev = self.first
        self.first.next = node
        node.next.prev = node
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            nodeToRemove = self.last.prev
            self.cache.pop(nodeToRemove.key)

            nodeToRemove.prev.next = nodeToRemove.next
            nodeToRemove.next.prev = nodeToRemove.prev
            



        
