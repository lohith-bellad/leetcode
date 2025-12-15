"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head: "Optional[Node]", insertVal: int) -> "Node":
        new_node = Node(insertVal)

        if head == None:
            new_node.next = new_node
            return new_node

        if head.next == head:
            head.next = new_node
            new_node.next = head
            return head

        cur = head
        while cur.next != head:
            if cur.val <= insertVal <= cur.next.val:
                break

            if cur.val > cur.next.val and (
                cur.val <= insertVal or insertVal <= cur.next.val
            ):
                break

            cur = cur.next

        new_node.next = cur.next
        cur.next = new_node

        return head
