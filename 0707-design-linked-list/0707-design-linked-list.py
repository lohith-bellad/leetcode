class DListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self.head = DListNode(-1)
        self.tail = DListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0

    def get(self, index: int) -> int:
        if index < 0 or index > self.count - 1:
            return -1

        cur_idx = 0
        cur_node = self.head.next

        while cur_idx < index:
            cur_node = cur_node.next
            cur_idx += 1

        return cur_node.val

    def addAtHead(self, val: int) -> None:
        new_node = DListNode(val)

        head_next = self.head.next
        self.head.next = new_node
        new_node.next = head_next
        new_node.prev = self.head
        head_next.prev = new_node
        self.count += 1
        return

    def addAtTail(self, val: int) -> None:
        new_node = DListNode(val)

        tail_prev = self.tail.prev
        self.tail.prev = new_node
        new_node.prev = tail_prev
        tail_prev.next = new_node
        new_node.next = self.tail
        self.count += 1
        return

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.count:
            return
        
        cur_idx = 0
        cur_node = self.head
        new_node = DListNode(val)

        while cur_idx < index:
            cur_idx += 1
            cur_node = cur_node.next
        
        cur_node_next = cur_node.next
        cur_node.next = new_node
        new_node.next = cur_node_next
        new_node.prev = cur_node
        cur_node_next.prev = new_node
        self.count += 1
        return


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.count - 1:
            return

        cur_idx = 0
        cur_node = self.head

        while cur_idx < index:
            cur_idx += 1
            cur_node = cur_node.next

        to_del = cur_node.next
        cur_node.next = to_del.next
        to_del.next.prev = cur_node
        self.count -= 1
        return
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)