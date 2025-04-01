# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def lprint(root):
            while root != None:
                print(root.val)
                root = root.next

        def reverse(root) -> ListNode:
            prev = None

            while root != None:
                temp = root.next
                root.next = prev
                prev = root
                root = temp
            
            return prev
        
        if head == None or head.next == None:
            return True

        slow = head
        fast = head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        temp = slow.next
        slow.next = None
        second_head = reverse(temp)

        lprint(head)
        while head and second_head:
            if head.val != second_head.val:
                return False
            head = head.next
            second_head = second_head.next
        
        if head != None:
            return head.next == None
        
        return True