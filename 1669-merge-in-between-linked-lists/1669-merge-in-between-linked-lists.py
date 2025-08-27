# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = list1
        prev = dummy
        count = 0
        root = list1

        while root != None:
            if count == a:
                break
            count += 1
            prev = root
            root = root.next
            
        tail = prev
        root = prev
        while root != None:
            if count == b + 1:
                break
            count += 1
            root = root.next

        next_head = root.next
        tail.next = list2

        while list2.next != None:
            list2 = list2.next
        
        list2.next = next_head

        return dummy.next

