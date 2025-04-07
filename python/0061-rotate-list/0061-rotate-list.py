# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return
            
        cnt = 0
        root = head

        while root != None:
            cnt += 1
            root = root.next
        
        rotation = k % cnt
        if rotation == 0:
            return head
        
        start = cnt - rotation

        root = head
        new_head = None
        idx = 0
        while root != None:
            idx += 1
            if idx == start:
                new_head = root.next
                root.next = None
                break
            root = root.next
        
        root = new_head
        while root.next != None:
            root = root.next
        
        root.next = head

        return new_head
