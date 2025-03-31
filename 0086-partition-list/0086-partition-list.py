# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        def lprint(root):
            while root != None:
                print(root.val)
                root = root.next

        left = ListNode(0)
        right = ListNode(0)

        root = head
        left_root = left
        right_root = right

        while root != None:
            if root.val < x:
                left_root.next = root
                left_root = root
            else:
                right_root.next = root
                right_root = root
            root = root.next
    
        right_root.next = None
        left_root.next = right.next

        return left.next