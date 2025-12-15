# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        temp = ListNode(0, head)
        prev = temp

        while fast.next != None and fast.next.next != None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if fast.next == None:
            prev.next = prev.next.next
        else:
            slow.next = slow.next.next

        return temp.next
