# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        if not head or not head.next:
            return head
        
        prev = head
        cur = head.next

        while cur != None:
            if prev.val == cur.val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        
        return head

        """
        dummy = ListNode(-200)
        dummy.next = head
        prev = dummy

        while head:
            if prev.val == head.val:
                head = head.next
            else:
                prev.next = head
                prev = head
                head = head.next
        prev.next = None
        
        return dummy.next