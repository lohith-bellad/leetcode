"""
428. Serialize and Deserialize N-ary Tree
Hard

Serialization is the process of converting a data structure or object into a
sequence of bits so that it can be stored in a file or memory buffer, or
transmitted across a network connection link to be reconstructed later in the
same or another computer environment.

Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree
is a rooted tree in which each node has no more than N children. There is no
restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that an N-ary tree can be serialized to a string and
this string can be deserialized to the original tree structure.

For example, you may serialize the following 3-ary tree:
            1
          / | \
         3  2  4
        / \
       5   6

as [1 [3[5 6] 2 4]]. Note that this is just an example, you do not necessarily
need to follow this format.

Or you can follow LeetCode's level order traversal serialization format, where
each group of children is separated by the null value.

For example, the above tree may be serialized as:
[1,null,3,2,4,null,5,6]


Constraints:
    * The number of nodes in the tree is in the range [0, 10^4].
    * 0 <= Node.val <= 10^4
    * The height of the n-ary tree is less than or equal to 1000
    * Do not use class member/global/static variables to store states. Your
      encode and decode algorithms should be stateless.

"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Codec:
    def serialize(self, root: "Node") -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        serial = []

        def traverse(head):
            if not head:
                return

            serial.append(str(head.val))
            serial.append("[")

            for i in range(len(head.children)):
                traverse(head.children[i])

            if not head.children:
                serial.pop()
            else:
                serial.append("]")

        serial.append("[")
        traverse(root)
        return " ".join(serial)

    def deserialize(self, data: str) -> "Node":
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if not data:
            return None

        deserial = data.split(" ")
        self.ind = 1

        def traverse():
            if self.ind >= len(deserial):
                return None

            child_val = int(deserial[self.ind])
            child_node = Node(child_val)
            self.ind += 1

            if self.ind < len(deserial) and deserial[self.ind] == "[":
                self.ind += 1

                while self.ind < len(deserial) and deserial[self.ind] != "]":
                    n = traverse()
                    if n:
                        child_node.children.append(n)

                if self.ind < len(deserial) and deserial[self.ind] == "]":
                    self.ind += 1

            return child_node

        return traverse()
