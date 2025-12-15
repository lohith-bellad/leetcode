# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        def list_reverse(root: ListNode):
            prev = None
            while root != None:
                temp = root.next
                root.next = prev
                prev = root
                root = temp
            return prev

        cnt = 1
        root = head
        dummy = ListNode(0)

        start = None
        prev = dummy
        broken_first = None
        broken_second = None
        while root != None:
            if cnt == left:
                start = root
                broken_first = prev
            if cnt == right:
                broken_second = root.next
                root.next = None
                break
            cnt += 1
            prev = root
            root = root.next

        new_head = list_reverse(start)

        temp = new_head
        while temp.next != None:
            temp = temp.next
        temp.next = broken_second

        if broken_first != dummy:
            broken_first.next = new_head
            return head
        else:
            return new_head
