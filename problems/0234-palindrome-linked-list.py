"""
234. Palindrome Linked List
Easy

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.


Example 1:
    Input: head = [1,2,2,1]
    Output: true

Example 2:
    Input: head = [1,2]
    Output: false


Constraints:
    * The number of nodes in the list is in the range [1, 10^5].
    * 0 <= Node.val <= 9

Follow-up: Could you do it in O(n) time and O(1) space?

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if not slow.next:
            return False

        second_head = slow.next

        prev = None
        while second_head:
            temp = second_head.next
            second_head.next = prev
            prev = second_head
            second_head = temp

        second_head = prev
        while second_head:
            if second_head.val != head.val:
                return False
            head = head.next
            second_head = second_head.next

        return True
