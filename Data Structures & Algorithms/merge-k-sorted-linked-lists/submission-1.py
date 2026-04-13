# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # keep the head of each list in a min-heap
        # insert the smallest head to the resulting list at each iter
        heap = []
        for i, head in enumerate(lists):
            heapq.heappush(heap, (head.val, i))

        curr = ListNode()
        head = curr
        while heap:
            (val, i) = heapq.heappop(heap)
            curr.next = lists[i]
            curr = curr.next
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))

        return head.next

        