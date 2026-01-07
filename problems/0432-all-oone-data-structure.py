"""
432. All O'one Data Structure
Hard

Design a data structure to store the strings' count with the ability to return
the strings with minimum and maximum counts.

Implement the AllOne class:
    * AllOne() Initializes the object of the data structure.
    * inc(String key) Increments the count of the string key by 1. If key does
      not exist in the data structure, insert it with count 1.
    * dec(String key) Decrements the count of the string key by 1. If the count
      of key is 0 after the decrement, remove it from the data structure. It is
      guaranteed that key exists in the data structure before the decrement.
    * getMaxKey() Returns one of the keys with the maximal count. If no element
      exists, return an empty string "".
    * getMinKey() Returns one of the keys with the minimum count. If no element
      exists, return an empty string "".

Note that each function must run in O(1) average time complexity.


Example 1:
    Input:
        ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
        [[], ["hello"], ["hello"], [], [], ["leet"], [], []]
    Output:
        [null, null, null, "hello", "hello", null, "hello", "leet"]
    Explanation:
        AllOne allOne = new AllOne();
        allOne.inc("hello");
        allOne.inc("hello");
        allOne.getMaxKey(); // return "hello"
        allOne.getMinKey(); // return "hello"
        allOne.inc("leet");
        allOne.getMaxKey(); // return "hello"
        allOne.getMinKey(); // return "leet"


Constraints:
    * 1 <= key.length <= 10
    * key consists of lowercase English letters.
    * It is guaranteed that for each call to dec, key is existing in the data
      structure.
    * At most 5 * 10^4 calls will be made to inc, dec, getMaxKey, and getMinKey.

"""


class Node:
    def __init__(self, count: int = 1):
        self.keys = set()
        self.count = count
        self.next = None
        self.prev = None


class AllOne:
    def __init__(self):
        self.key_table = {}
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        if key in self.key_table:
            node = self.key_table[key]
            node.keys.remove(key)
            count = node.count

            next_node = node.next
            if next_node == self.tail or next_node.count != count + 1:
                new_node = Node(count + 1)
                new_node.keys.add(key)
                new_node.next = next_node
                new_node.prev = node
                node.next = new_node
                next_node.prev = new_node
                self.key_table[key] = new_node
            else:
                next_node.keys.add(key)
                self.key_table[key] = next_node

            if not node.keys:
                self.remove_node(node)
        else:
            next_node = self.head.next
            if next_node == self.tail or next_node.count > 1:
                new_node = Node(1)
                new_node.keys.add(key)
                new_node.next = next_node
                new_node.prev = self.head
                self.head.next = new_node
                next_node.prev = new_node
                self.key_table[key] = new_node
            else:
                next_node.keys.add(key)
                self.key_table[key] = next_node

    def dec(self, key: str) -> None:
        if key not in self.key_table:
            return

        node = self.key_table[key]
        count = node.count
        node.keys.remove(key)

        if count == 1:
            del self.key_table[key]
        else:
            prev_node = node.prev
            if prev_node == self.head or prev_node.count != count - 1:
                new_node = Node(count - 1)
                new_node.keys.add(key)
                new_node.prev = prev_node
                new_node.next = node
                prev_node.next = new_node
                node.prev = new_node
                self.key_table[key] = new_node
            else:
                prev_node.keys.add(key)
                self.key_table[key] = prev_node

        if not node.keys:
            self.remove_node(node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""

        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""

        return next(iter(self.head.next.keys))

    def remove_node(self, node: Node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node
