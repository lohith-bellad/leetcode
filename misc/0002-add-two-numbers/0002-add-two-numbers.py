# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        prev = dummy
        carry = 0

        while l1 != None or l2 != None:
            n1 = 0
            n2 = 0
            if l1 != None:
                n1 = l1.val
            if l2 != None:
                n2 = l2.val

            tot = n1 + n2 + carry
            carry = tot // 10
            tot = tot % 10
        
            prev.next = ListNode(tot)
            prev = prev.next

            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next

        if carry > 0:
            prev.next = ListNode(carry)

        return dummy.next