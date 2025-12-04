"""
143. Reorder List
Medium

You are given the head of a singly linked-list. The list can be represented as:

    L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.


Example 1:
    Input: head = [1,2,3,4]
    Output: [1,4,2,3]

Example 2:
    Input: head = [1,2,3,4,5]
    Output: [1,5,2,4,3]


Constraints:
    * The number of nodes in the list is in the range [1, 5 * 10^4].
    * 1 <= Node.val <= 1000

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        headB = slow.next
        slow.next = None
        prev = None

        while headB:
            temp = headB.next
            headB.next = prev
            prev = headB
            headB = temp

        headB = prev
        headA = head

        while headB:
            temp = headA.next
            headA.next = headB
            headB = headB.next
            headA.next.next = temp
            headA = temp

        return
