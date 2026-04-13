class ListNode:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self, head = None, tail = None):
        self.head = ListNode(-1, -1, None, None)
        self.tail = ListNode(-1, -1, self.head, None)
        self.head.next = self.tail
        self.map = dict()

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.list = LinkedList()
        

    def get(self, key: int) -> int:
        if key in self.list.map:
            # move key to head
            key_node = self.list.map[key]
            key_node.prev.next = key_node.next
            key_node.next.prev = key_node.prev
            
            self.list.head.next.prev = key_node
            key_node.next = self.list.head.next
            key_node.prev = self.list.head
            self.list.head.next = key_node
            print(f"get({key}) {self.list.map[key].val}  | {self.list.head.next.key} {self.list.tail.prev.key} | {self.list.map}")
            return self.list.map[key].val
        print(f"get({key}) -1 | {self.list.head.next.key} {self.list.tail.prev.key} | {self.list.map}")
        return -1        


    def put(self, key: int, value: int) -> None:
        print(f"put({key}, {value}) | ", end="")
        if len(self.list.map) >= self.capacity and key not in self.list.map:
            # remove LRU
            # lru = self.list.tail.prev
            # self.list.map.pop(lru.key)
            # lru.prev.next = self.list.tail
            # self.list.tail.prev = lru.prev

            self.list.map.pop(self.list.tail.prev.key)
            self.list.tail.prev.prev.next = self.list.tail
            self.list.tail.prev = self.list.tail.prev.prev
        if key in self.list.map:
            # move key to head
            key_node = self.list.map[key]
            key_node.val = value
            key_node.prev.next = key_node.next
            key_node.next.prev = key_node.prev
            
            self.list.head.next.prev = key_node
            key_node.next = self.list.head.next
            key_node.prev = self.list.head
            self.list.head.next = key_node
        else:
            # create node on the head
            key_node = ListNode(key, value, self.list.head, self.list.head.next)
            self.list.head.next.prev = key_node
            self.list.head.next = key_node
            self.list.map[key] = key_node
        print(f"{self.list.head.next.key} {self.list.tail.prev.key} | {self.list.map}")
        
