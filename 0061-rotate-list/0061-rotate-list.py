# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
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
        
        if not head or k == 0 or not head.next:
            return head

        count = 0
        root = head
        tail = None

        while root:
            count += 1
            if root.next == None:
                tail = root
            root = root.next

        rval = k % count
        if rval == 0:
            return head
        rval = count - rval
        root = head
        prev = None

        while root and rval > 0:
            prev = root
            root = root.next
            rval -= 1

        if prev and tail:
            prev.next = None
            tail.next = head

        return root
        """
        if not head or not head.next:
            return head
            
        count = 0
        root = head
        tail = None

        while root:
            count += 1
            if not root.next:
                tail = root
            root = root.next
        
        # create a loop
        tail.next = head

        rot_head = count - (k % count)
        dummy = ListNode(-200)
        dummy.next = head
        prev = dummy
        cur_head = head

        while rot_head > 0:
            prev = cur_head
            cur_head = cur_head.next
            rot_head -= 1
        
        prev.next = None
        return cur_head

