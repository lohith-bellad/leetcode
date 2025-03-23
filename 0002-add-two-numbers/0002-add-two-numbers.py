# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        suma = 0 
        carry = 0
        dummy = ListNode()
        output = dummy
        ptr = None

        while l1 != None and l2 != None:
            add = l1.val + l2.val + carry
            suma = add % 10
            carry = add // 10

            output.next = ListNode(suma)
            l1 = l1.next
            l2 = l2.next
            output = output.next
        
        if l1 == None:
            ptr = l2
        else:
            ptr = l1

        while ptr != None:
            add = ptr.val + carry
            suma = add % 10
            carry = add // 10

            output.next = ListNode(suma)
            ptr = ptr.next
            output = output.next

        if carry > 0:
            output.next = ListNode(carry)
        
        return dummy.next