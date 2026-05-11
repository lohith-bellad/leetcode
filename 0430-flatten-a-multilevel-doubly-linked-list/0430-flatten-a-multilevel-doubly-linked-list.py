"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        my_stack = []

        dummy = ListNode(-1)
        #dummy.next = head
        prev = dummy

        my_stack.append(head)

        while len(my_stack):
            cur_head = my_stack.pop()

            while cur_head != None:
                prev.next = cur_head
                cur_head.prev = prev
                prev = prev.next

                if cur_head.child != None:
                    if cur_head.next != None:
                        my_stack.append(cur_head.next)
                    temp = cur_head.child
                    cur_head.child = None
                    cur_head = temp

                else:
                    cur_head = cur_head.next
        
        dummy.next.prev = None
        return dummy.next

