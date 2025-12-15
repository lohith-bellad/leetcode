# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = 0
        root = head

        while root != None:
            root = root.next
            nodes += 1

        if nodes == 1:
            return None

        if n > nodes:
            return

        ind_to_remove = nodes - n
        dummy = ListNode(0)
        dummy.next = head
        root = dummy

        while ind_to_remove > 0:
            root = root.next
            ind_to_remove -= 1

        if root.next == None:
            return head

        root.next = root.next.next

        return dummy.next
