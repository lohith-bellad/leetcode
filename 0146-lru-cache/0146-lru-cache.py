class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.table:
            self.remove_node(self.table[key])
            self.add_node(self.table[key])
            return self.table[key].val
        
        return -1
    
    def remove_node(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add_node(self, node: Node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            old_node = self.table[key]
            self.remove_node(old_node)
        
        new_node = Node(key, value)
        self.table[key] = new_node
        self.add_node(new_node)

        if len(self.table) > self.capacity:
            del_node = self.head.next
            self.remove_node(del_node)
            del self.table[del_node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)