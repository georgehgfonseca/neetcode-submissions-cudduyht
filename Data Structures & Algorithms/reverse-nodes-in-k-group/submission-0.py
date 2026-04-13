# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Count length
        n = 0
        curr = head
        while curr:
            curr = curr.next
            n += 1

        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy
        curr = head

        while n >= k:
            group_prev = None
            group_head = curr

            # Reverse k nodes
            for _ in range(k):
                temp = curr.next
                curr.next = group_prev
                group_prev = curr
                curr = temp

            # Connect previous group to reversed
            prev_group_tail.next = group_prev
            group_head.next = curr  # connect tail to next part

            # Move prev_group_tail to the end of the reversed group
            prev_group_tail = group_head
            n -= k

        return dummy.next


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # compute list length
        n = 0 # list length
        curr = head
        while curr:
            curr = curr.next
            n += 1

        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy
        curr = head
        # while remaining pos >= k
        while n >= k:
            group_prev = None
            group_head = curr

            # reverse the list k times, then save the tail
            for _ in range(k):
                temp = curr.next
                curr.next = group_prev
                group_prev = curr
                curr = temp
            
            # link the tail of prev list list to the head of curr list
            # connect previous gruop to reversed
            prev_group_tail.next = group_prev
            group_head.next = curr
            prev_group_tail = group_head

            n -= k
        
        return dummy.next