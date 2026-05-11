# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        def list_reverse(root: ListNode):
            prev = None
            while root != None:
                temp = root.next
                root.next = prev
                prev = root
                root = temp
            return prev

        cnt = 1
        root = head
        dummy = ListNode(0)

        start = None
        prev = dummy
        broken_first = None
        broken_second = None
        while root != None:
            if cnt == left:
                start = root
                broken_first = prev
            if cnt == right:
                broken_second = root.next
                root.next = None
                break
            cnt += 1
            prev = root
            root = root.next
        
        new_head = list_reverse(start)

        temp = new_head
        while temp.next != None:
            temp = temp.next
        temp.next = broken_second

        if broken_first != dummy:
            broken_first.next = new_head
            return head
        else:
            return new_head
        """
        def reverse_list(node):
            prev = None
            while node:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            return prev
    
        if not head or left == right:
            return head
        
        dummy = ListNode(-600)
        dummy.next = head
        cur_ind = 1
        prev = dummy
        start = None
        end = None
        first_list_tail = None
        second_list_head = None

        while head:
            if cur_ind == left:
                start = head
                first_list_tail = prev
            elif cur_ind == right:
                end = head
                second_list_head = head.next
                break
            
            prev = head
            head = head.next
            cur_ind += 1
        
        end.next = None
        rev_head = reverse_list(start)
        root = rev_head
        while root.next:
            root = root.next

        root.next = second_list_head
        first_list_tail.next = rev_head

        return dummy.next

        