class Tree_Node(object):
	def __init__(self, val=None, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Instance_Count_Tree_Node(Tree_Node):
	def __init__(self, value):
		super(Instance_Count_Tree_Node, self).__init__(value)
		self.instances = 1

class Binary_Search_Tree_Iterative(object):
	def __init__(self):
		self.root = None
		self._size = 0

	def insert(self, value):
		new_node = Instance_Count_Tree_Node(value)
		self._size += 1

		if self.root == None:
			self.root = new_node
			return

		from collections import deque
		stack = deque([self.root])
		
		while stack:
			if stack[-1] == None:
				stack.pop()
				if new_node.val < stack[-1].val:
					stack[-1].left = new_node
				elif new_node.val > stack[-1].val:
					stack[-1].right = new_node
				else:
					stack[-1].instances += 1
				break
			if new_node.val < stack[-1].val:
				stack.append(stack[-1].left)
			else:
				stack.append(stack[-1].right)

	def print_tree(self):
		if self.root == None:
			return
		from collections import deque
		current = self.root
		stack = deque()
		while True:
			if current != None:
				stack.append(current)
				current = current.left
			else:
				if stack:
					current = stack.pop()
					for i in xrange(current.instances):
						pass#print current.val
					current = current.right
				else:
					break
if __name__ == "__main__":
	t = Binary_Search_Tree_Iterative()
	t.insert(10)
	t.insert(5)
	t.insert(15)
	t.insert(5)
	t.print_tree()
	print
	t.print_tree_two()
