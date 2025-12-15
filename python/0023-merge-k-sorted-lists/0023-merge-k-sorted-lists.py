# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        prev = dummy
        min_heap = []

        for i in range(len(lists)):
            if lists[i] != None:
                heapq.heappush(min_heap, (lists[i].val, i, lists[i]))

        while len(min_heap) > 0:
            _, _, min_head = heapq.heappop(min_heap)
            prev.next = min_head
            prev = prev.next
            min_head = min_head.next
            if min_head != None:
                i += 1
                heapq.heappush(min_heap, (min_head.val, i, min_head))

        return dummy.next
