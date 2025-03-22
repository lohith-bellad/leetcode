# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        c1 = head

        def reverse(head: Optional[ListNode]) -> ListNode:
            prev = None

            while head != None:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            
            return prev

        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next

        c2 = reverse(slow.next)
        slow.next = None

        max_twin = 0
        while c1 != None and c2 != None:
            max_twin = max(max_twin, c1.val + c2.val)
            c1 = c1.next
            c2 = c2.next
        
        return max_twin
        