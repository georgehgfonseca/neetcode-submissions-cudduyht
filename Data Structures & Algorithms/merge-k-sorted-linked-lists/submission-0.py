# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [lst for lst in lists if lst]  # Filter out empty lists
        if not lists:
            return None

        dummy = ListNode()
        res = dummy

        while lists:
            iMin = 0
            for i in range(1, len(lists)):
                if lists[i].val < lists[iMin].val:
                    iMin = i

            dummy.next = lists[iMin]
            dummy = dummy.next
            lists[iMin] = lists[iMin].next

            if not lists[iMin]:
                lists.pop(iMin)

        return res.next
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # must be O(1) space...
        lists = [lst for lst in lists if lst]  # Filter out empty lists
        if not lists:
            return None

        head = ListNode() # dummy node
        res = head
        while True:
            # pick the smallest head
            iMin = 0
            for i in range(len(lists)):
                if lists[i].val < lists[iMin].val:
                    iMin = i
            head.next = lists[iMin]
            head = head.next
            lists[iMin] = lists[iMin].next
            if not lists[iMin]:
                lists.pop(iMin)
            if not lists:
                break
        return res.next
