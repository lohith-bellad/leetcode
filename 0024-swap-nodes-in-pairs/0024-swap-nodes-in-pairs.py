# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head

        while cur != None and cur.next != None:
            first = cur
            second = cur.next
            prev.next = second
            temp = second.next
            second.next = first
            first.next = temp
            prev = first
            cur = temp
        
        return dummy.next