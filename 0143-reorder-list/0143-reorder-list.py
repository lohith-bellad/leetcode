# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def reverse(head: ListNode) -> ListNode:
            prev = None

            while head != None:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            
            return prev

        if head.next == None or head.next.next == None:
            return None

        slow = head
        fast = head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        
        second_head = reverse(slow.next)
        slow.next = None
        first_head = head

        dummy = ListNode(0)
        root = dummy

        while first_head != None and second_head != None:
            root.next = first_head
            temp = first_head.next
            first_head.next = second_head
            root = second_head
            second_head = second_head.next
            first_head = temp
        
        if first_head != None:
            root.next = first_head
        
        return None