"""
297. Serialize and Deserialize Binary Tree
Hard

Serialization is the process of converting a data structure or object into a
sequence of bits so that it can be stored in a file or memory buffer, or
transmitted across a network connection link to be reconstructed later in the
same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no
restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and
this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes
a binary tree. You do not necessarily need to follow this format, so please be
creative and come up with different approaches yourself.


Example 1:
    Input: root = [1,2,3,null,null,4,5]
        Tree structure:
            1
           / \
          2   3
             / \
            4   5
    Output: [1,2,3,null,null,4,5]

Example 2:
    Input: root = []
    Output: []


Constraints:
    * The number of nodes in the tree is in the range [0, 10^4].
    * -1000 <= Node.val <= 1000

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        serial = []

        def traverse(head):
            if not head:
                return

            serial.append(str(head.val))

            if head.right:
                serial.append("[")
                traverse(head.left)
                serial.append("]")

                serial.append("[")
                traverse(head.right)
                serial.append("]")
            elif head.left:
                serial.append("[")
                traverse(head.left)
                serial.append("]")

            return

        traverse(root)
        return "".join(serial)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        deserial = data.split("")

        def traverse(ind):
            pivot = ind

            while ind < len(deserial) and (
                deserial[pivot].isdigit() or deserial[pivot] == "-"
            ):
                pivot += 1

            if deserial[ind:pivot] == "":
                return None, pivot + 1

            num = int(deserial[ind:pivot])
            new_node = TreeNode(num)

            if ind < len(deserial) and deserial[ind] == "[":
                new_node.left, ind = traverse(ind + 1)

            if ind < len(deserial) and deserial[ind] == "[":
                new_node.right, ind = traverse(ind + 1)

            return new_node, ind + 1

        if len(data) == 0:
            return None

        head, _ = traverse(0)
        return head
