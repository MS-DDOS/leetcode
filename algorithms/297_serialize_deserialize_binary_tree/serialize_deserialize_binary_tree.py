# Definition for a binary tree node.
class TreeNode(object):
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
        if not root:
            return ""
        serialized = []
        return ','.join(self.traverse(root, serialized))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []
        return self.detraverse(data.split(','))

    def traverse(self, root, serialized):
        if not root:
            return serialized.append("!")
        serialized.append(str(root.val))
        self.traverse(root.left,serialized)
        self.traverse(root.right,serialized)
        return serialized

    def detraverse(self, data):
        if data[0] == "!":
            data.remove(data[0])
            return None
        node = TreeNode(int(data[0]))
        data.remove(data[0])
        node.left = self.detraverse(data)
        node.right = self.detraverse(data)
        return node

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    solver = Codec()
    s = solver.serialize(root)
    print s
    print s.split(',')
    head = solver.deserialize(solver.serialize(root))
    print head.val
    print head.left.val
    print head.right.val
    print head.right.left.val
    print head.right.right.val

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))