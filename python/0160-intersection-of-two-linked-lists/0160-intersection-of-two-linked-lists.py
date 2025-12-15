# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        cnt1 = 0
        root = headA

        while root != None:
            cnt1 += 1
            root = root.next

        cnt2 = 0
        root = headB

        while root != None:
            cnt2 += 1
            root = root.next

        left = headA
        right = headB
        if cnt1 > cnt2:
            diff = cnt1 - cnt2
            while diff > 0:
                left = left.next
                diff -= 1
        else:
            diff = cnt2 - cnt1
            while diff > 0:
                right = right.next
                diff -= 1

        while left != right:
            left = left.next
            right = right.next

        return left
