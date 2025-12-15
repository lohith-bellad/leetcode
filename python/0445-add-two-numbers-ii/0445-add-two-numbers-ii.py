# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def reverse(root: ListNode) -> ListNode:
            prev = None

            while root != None:
                temp = root.next
                root.next = prev
                prev = root
                root = temp

            return prev

        l1_rev = reverse(l1)
        l2_rev = reverse(l2)

        dummy = ListNode(0)
        head = dummy
        carry = 0

        while l1_rev != None and l2_rev != None:
            s = l1_rev.val + l2_rev.val + carry
            carry = s // 10
            s = s % 10
            head.next = ListNode(s, None)
            head = head.next
            l1_rev = l1_rev.next
            l2_rev = l2_rev.next

        l_rev = None
        if l1_rev != None:
            l_rev = l1_rev
        elif l2_rev != None:
            l_rev = l2_rev

        while l_rev != None:
            s = l_rev.val + carry
            carry = s // 10
            s = s % 10
            head.next = ListNode(s, None)
            head = head.next
            l_rev = l_rev.next

        if carry > 0:
            head.next = ListNode(carry, None)

        return reverse(dummy.next)
