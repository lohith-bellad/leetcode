"""
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        self.freq = 1
class DLinkedList:
    def __init__(self):
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def append(self, node):
        prev, next = self.tail.prev, self.tail
        prev.next = node
        next.prev = node
        node.prev, node.next = prev, next
        self.size += 1
    
    def pop(self, node=None):
        if node is None:
            node = self.head.next
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        self.size -= 1
        return node

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key2val = {}
        self.freq2key = {}
        self.min_freq = 0
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.key2val:
            return -1
        node = self.key2val[key]
        freq = node.freq
        self.freq2key[freq].pop(node)
        if self.min_freq == freq and self.freq2key[freq].size == 0:
            self.min_freq += 1
        node.freq += 1
        if node.freq not in self.freq2key:
            self.freq2key[node.freq] = DLinkedList()
        self.freq2key[node.freq].append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key2val:
            node = self.key2val[key]
            self.get(key)
            node.val = value
        else:
            if self.size == self.capacity:
                node = self.freq2key[self.min_freq].pop()
                del self.key2val[node.key]
                self.size -= 1
            node = ListNode(key, value)
            self.key2val[key] = node
            if 1 not in self.freq2key:
                self.freq2key[1] = DLinkedList()
            self.freq2key[1].append(node)
            self.min_freq = 1
            self.size += 1

"""
class ListNode:
    def __init__(self, key: int, val: int):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
        self.freq = 1

class DLinkedList:
    def __init__(self):
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.count = 0
        self.head.next = self.tail
        self.tail.prev = self.head
    
    # Append at tail
    def append(self, node: ListNode):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        self.tail.prev = node
        node.next = self.tail
        self.count += 1
    
    def pop(self, node: ListNode = None):
        if not node:
            node = self.head.next
        prev_node = node.prev
        next_node = node.next
        prev_node.next = node.next
        next_node.prev = prev_node
        self.count -= 1
        return node

class LFUCache:
    def __init__(self, capacity: int):
        self.key_store = {}
        self.freq_store = {}
        self.capacity = capacity
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key_store:
            return -1
        
        node = self.key_store[key]
        
        # Remove node from cur_freq level and
        # upgrade to next higher freq level
        freq_list = self.freq_store[node.freq]
        freq_list.pop(node)
        if node.freq == self.min_freq and freq_list.count == 0:
            self.min_freq += 1
        node.freq += 1
        if node.freq not in self.freq_store:
            self.freq_store[node.freq] = DLinkedList()
        self.freq_store[node.freq].append(node)
        return node.val
    
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.key_store:
            node = self.key_store[key]
            node.val = value
            self.get(key)
        else:
            new_node = ListNode(key, value)
            if len(self.key_store) == self.capacity:
                node = self.freq_store[self.min_freq].pop()
                del self.key_store[node.key]
            self.key_store[key] = new_node
            if 1 not in self.freq_store:
                self.freq_store[1] = DLinkedList()
            self.freq_store[1].append(new_node)
            self.min_freq = 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)