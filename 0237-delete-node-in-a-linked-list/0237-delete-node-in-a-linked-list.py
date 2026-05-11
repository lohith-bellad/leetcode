# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        
        prev = node
        cur_node = node.next

        while cur_node != None:
            prev.val = cur_node.val
            if cur_node.next == None:
                prev.next = None
                break
            prev = cur_node
            cur_node = cur_node.next

        return
        """
        while node.next and node.next.next:
            node.val = node.next.val
            node = node.next
        
        node.val = node.next.val
        node.next = None

        return 