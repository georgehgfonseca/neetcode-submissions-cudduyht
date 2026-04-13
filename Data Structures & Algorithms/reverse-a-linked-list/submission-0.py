# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev, curr = None, head
        while curr.next:
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
        curr.next = prev
        return curr
        
        # create a prev node, link it to head
        # iterate over head reversing the links


        