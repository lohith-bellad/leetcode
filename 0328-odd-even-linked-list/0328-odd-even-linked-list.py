# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        if head == None or head.next == None:
            return head

        odd = head
        even = head.next
        even_head = head.next

        while even.next != None and even.next.next != None:
            odd.next = even.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
            
        if even.next == None:
            odd.next = even_head
        else:
            odd.next = even.next
            even.next = None
            odd.next.next = even_head

        return head
        """
        odd_list = ListNode(-1)
        odd_prev = odd_list
        even_list = ListNode(-1)
        even_prev = even_list
        cur_ind = 1

        while head:
            if cur_ind % 2 == 1:
                odd_prev.next = head
                odd_prev = odd_prev.next
            else:
                even_prev.next = head
                even_prev = even_prev.next
            head = head.next
            cur_ind += 1
        
        even_prev.next = None
        odd_prev.next = even_list.next

        return odd_list.next