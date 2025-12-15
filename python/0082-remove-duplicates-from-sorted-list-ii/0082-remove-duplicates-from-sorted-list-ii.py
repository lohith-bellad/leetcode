# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float("-inf"))
        dups = set()
        prev = dummy
        root = head

        while root != None:
            if root.val != prev.val:
                prev.next = root
                prev = root
                root = root.next
            else:
                dups.add(root.val)
                root = root.next

        prev = dummy
        root = head

        while root != None:
            if root.val not in dups:
                prev.next = root
                prev = root
                root = root.next
            else:
                root = root.next
        prev.next = root

        return dummy.next
