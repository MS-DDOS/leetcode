import treenodes

class ThreadedTree(object):
	def __init__(self, root=None, duplicate_strategy="stack"):
		"""Creates an empty threaded tree.

		Duplicate Strategy:
		stack - aggregate duplicate keys using an integer
		duplicate - allow duplicate nodes in tree
		"""
		self.root = root
		self._len = 0
		self.duplicate_strategy = duplicate_strategy

	def __len__(self):
		return self._len

	def new_node(self, value):
		"""Seperated into a method so that we can return different types of nodes for different situations"""
		return treenodes.Threaded_Tree_Node(value)

	def insert(self, value):
		"""Inserts a new node containing 'value' into the tree."""
		self._len += 1

		if self.root == None:
			self.root = self.new_node(value)
			return True

		current = self.root
		directionLeft = False
		directionRight = False

		while True:
			if current.val > value:
				if not current.lthreaded:
					#Add as left child
					directionLeft = True
					directionRight = False
					break
				else:
					current = current.left
			elif current.val < value:
				if not current.rthreaded:
					directionLeft = False
					directionRight = True
					break
				else:
					current = current.right

		if directionLeft:
			new_node = self.new_node(value)
			new_node.left = current.left
			current.left = new_node
			new_node.lthreaded = current.lthreaded
			current.lthreaded = True
			new_node.right = current
		elif directionRight:
			new_node = self.new_node(value)
			new_node.right = current.right
			current.right = new_node
			new_node.rthreaded = current.rthreaded
			current.rthreaded = True
			new_node.left = current

	def in_order(self):
		current = self.root
		while current.lthreaded:
			current = current.left
		while current != None:
			pass#print current.val
			current = self.findNextInorder(current)

	def findNextInorder(self, node):
		if not node.rthreaded:
			return node.right

		node = node.right

		while node.lthreaded:
			node = node.left
		return node

if __name__ == "__main__":
	t = ThreadedTree()
	t.insert(25)
	t.insert(10)
	t.insert(5)
	t.insert(15)
	t.in_order()