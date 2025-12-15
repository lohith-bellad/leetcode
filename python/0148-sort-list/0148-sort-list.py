# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_mid(self, root: ListNode) -> ListNode:
        slow = root
        fast = root

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        dummy = ListNode(0)
        prev = dummy

        while left != None and right != None:
            if left.val < right.val:
                prev.next = left
                left = left.next
            else:
                prev.next = right
                right = right.next
            prev = prev.next

        prev.next = left if left else right

        return dummy.next

    def lprint(self, root: ListNode):
        while root != None:
            print(root.val)
            root = root.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        mid = self.get_mid(head)
        second = mid.next
        mid.next = None

        left = self.sortList(head)
        right = self.sortList(second)

        temp = self.merge(left, right)
        return temp
