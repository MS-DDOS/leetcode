class Tree_Node(object):
	def __init__(self, val=None, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Instance_Count_Tree_Node(Tree_Node):
	def __init__(self, value):
		super(Instance_Count_Tree_Node, self).__init__(value)
		self.instances = 1

class Binary_Search_Tree(object):
	def __init__(self):
		self.root = None
		self._size = 0

	def insert(self, value):
		new_node = Instance_Count_Tree_Node(value)
		if self.root == None:
			self.root = new_node
			self._size = 1
		else:
			self._insert(self.root, new_node)
			self._size += 1

	def _insert(self, node, value):
		if node == None:
			return value

		if value.val < node.val:
			node.left = self._insert(node.left, value)
		elif value.val > node.val:
			node.right = self._insert(node.right, value)
		else:
			node.instances += 1
		return node

	def print_tree(self):
		self._print_tree(self.root)

	def _print_tree(self, node):
		if node == None:
			return
		self._print_tree(node.left)
		for i in xrange(node.instances):
			pass#print node.val
		self._print_tree(node.right)

	def contains(self, value):
		return self._contains(self.root, value)

	def _contains(self, root, value):
		if root == None:
			return False
		if value == root.val:
			return True
		elif value < root.val:
			return self._contains(root.left, value)
		else:
			return self._contains(root.right, value)

	def size(self):
		return self._size

	def max_depth(self):
		return self._max_depth(self.root, 0, 0)

	def _max_depth(self, root, current_depth, max_depth):
		if root == None:
			return max_depth
		if current_depth > max_depth:
			max_depth = current_depth
		left_max = self._max_depth(root.left, current_depth + 1, max_depth)
		right_max = self._max_depth(root.right, current_depth + 1, max_depth)
		return max(left_max, right_max)


if __name__ == "__main__":
	t = Binary_Search_Tree()
	t.insert(10)
	t.insert(5)
	t.insert(15)
	t.insert(15)
	t.insert(13)
	t.insert(20)
	t.insert(15)
	t.print_tree()
	print
	print t.max_depth()
	print t.size()
	print t.contains(13)
	print t.contains(17)