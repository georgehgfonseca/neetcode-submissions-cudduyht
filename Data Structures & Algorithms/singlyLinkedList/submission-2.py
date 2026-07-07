class ListNode:

    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
        # self.tail = None
        self.length = 0

    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1

        curr = self.head
        for _ in range(index):
            curr = curr.next
        
        return curr.val


    def insertHead(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
        else:
            node = ListNode(val, self.head)
            self.head = node

        self.length += 1

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
            self.length += 1
            return

        # can be improved to O(1)
        prev = None
        curr = self.head
        while curr:
            prev, curr = curr, curr.next
        
        self.length += 1
        prev.next = ListNode(val)

    def remove_op(self, node: ListNode):
        del node
        self.length -= 1
        if self.length == 0:
            self.head = None

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.length:
            print("Invalid index")
            return False

        if index == 0:
            temp = self.head
            self.head = self.head.next
            self.remove_op(temp)
            return True

        if index == 1:
            temp = self.head.next
            self.head.next = self.head.next.next
            self.remove_op(temp)
            return True

        prev = None
        curr = self.head
        for i in range(index + 1):
            if not curr:
                return False

            if i == index:
                temp = curr
                prev.next = curr.next
                self.remove_op(temp)
                return True
            
            prev, curr = curr, curr.next

        return False

    def getValues(self) -> List[int]:
        res = []
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        
        return res
        
