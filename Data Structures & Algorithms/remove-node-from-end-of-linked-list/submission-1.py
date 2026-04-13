# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1:
            temp = head
            prev = None
            while head.next:
                prev = head
                head = head.next
            if not prev:
                return prev
            prev.next = None
            return temp

        head = self.reverseList(head)
        temp = head

        i = 1
        prev = None
        while head and i < n:
            prev = head
            head = head.next
            i += 1
        prev.next = head.next

        return self.reverseList(temp)
        