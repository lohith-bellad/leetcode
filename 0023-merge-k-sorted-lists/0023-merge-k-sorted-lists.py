# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(minHeap, (lists[i].val, i, lists[i]))
        
        dummy = ListNode(-1)
        prev = dummy

        while minHeap:
            _, i, cur_node = heapq.heappop(minHeap)
            prev.next = cur_node
            prev = cur_node

            if cur_node.next:
                next_node = cur_node.next
                heapq.heappush(minHeap, (next_node.val, i + 100, next_node))
        
        prev.next = None

        return dummy.next
