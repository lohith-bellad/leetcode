"""
146. LRU Cache
Medium

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
    * LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    * int get(int key) Return the value of the key if the key exists, otherwise return -1.
    * void put(int key, int value) Update the value of the key if the key exists.
      Otherwise, add the key-value pair to the cache. If the number of keys exceeds
      the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.


Example 1:
    Input:
        ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
        [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    Output:
        [null, null, null, 1, null, -1, null, -1, 3, 4]

    Explanation:
        LRUCache lRUCache = new LRUCache(2);
        lRUCache.put(1, 1); // cache is {1=1}
        lRUCache.put(2, 2); // cache is {1=1, 2=2}
        lRUCache.get(1);    // return 1
        lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
        lRUCache.get(2);    // returns -1 (not found)
        lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
        lRUCache.get(1);    // return -1 (not found)
        lRUCache.get(3);    // return 3
        lRUCache.get(4);    // return 4


Constraints:
    * 1 <= capacity <= 3000
    * 0 <= key <= 10^4
    * 0 <= value <= 10^5
    * At most 2 * 10^5 calls will be made to get and put.

"""


class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.node_table = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    # Add node to the tail
    def add_node(self, node: Node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.next = self.tail
        node.prev = prev_node
        self.tail.prev = node

    # Remove node from the list
    def remove_node(self, node: Node):
        next_node = node.next
        prev_node = node.prev
        next_node.prev = prev_node
        prev_node.next = next_node

    def get(self, key: int) -> int:
        if key in self.node_table:
            node = self.node_table[key]
            val = node.val
            self.remove_node(node)
            self.add_node(node)
            return val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.node_table:
            node = self.node_table[key]
            node.val = value
            self.remove_node(node)
            self.add_node(node)
            return

        new_node = Node(key, value)
        if len(self.node_table) == self.capacity:
            bad_node = self.head.next
            self.remove_node(bad_node)
            del self.node_table[bad_node.key]
        self.node_table[key] = new_node
        self.add_node(new_node)

        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
