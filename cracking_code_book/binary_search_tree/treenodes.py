class Tree_Node(object):
	def __init__(self, val=None, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Instance_Count_Tree_Node(Tree_Node):
	def __init__(self, value):
		super(Instance_Count_Tree_Node, self).__init__(value)
		self.instances = 1

class Threaded_Tree_Node(Tree_Node):
	def __init__(self, value):
		super(Threaded_Tree_Node, self).__init__(value)
		self.rthreaded = False #indicates that the right pointer is to a predescessor, not a descendant
		self.lthreaded = False

class Instance_Count_Threaded_Tree_Node(Instance_Count_Tree_Node, Threaded_Tree_Node):
	def __init__(self, value):
		super(Instance_Count_Threaded_Tree_Node, self).__init__(value)